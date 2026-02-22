#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import os
import pathlib
import re
import subprocess
import sys
import textwrap

ROOT = pathlib.Path('/Users/bob/.openclaw/workspace')
RUNTIME = ROOT / '.runtime' / 'youtube'
OUTDIR = ROOT / 'research' / 'youtube'
VENV_PY = ROOT / '.venv-stt' / 'bin' / 'python3'
YTDLP = str(ROOT / '.venv-stt' / 'bin' / 'yt-dlp')


def run(cmd, input_text=None, check=True):
    p = subprocess.run(
        cmd,
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
    )
    if check and p.returncode != 0:
        raise RuntimeError(f"cmd failed: {' '.join(cmd)}\n{p.stderr[:800]}")
    return p


def sanitize(s: str) -> str:
    s = re.sub(r'[^a-zA-Z0-9-_ ]+', '', s or '').strip().replace(' ', '-')
    return s[:80] or 'video'


def get_meta(url: str):
    p = run([YTDLP, '-J', '--no-warnings', url])
    return json.loads(p.stdout)


def download_audio(url: str, vid: str):
    RUNTIME.mkdir(parents=True, exist_ok=True)
    outtmpl = str(RUNTIME / f'{vid}.%(ext)s')
    run([YTDLP, '-f', 'bestaudio', '-x', '--audio-format', 'm4a', '--output', outtmpl, '--no-playlist', url])
    cands = sorted(RUNTIME.glob(f'{vid}.*'))
    if not cands:
        raise RuntimeError('no audio file downloaded')
    return str(cands[-1])


def transcribe(audio_path: str, model='base'):
    script = textwrap.dedent(
        f'''
        from faster_whisper import WhisperModel
        m=WhisperModel('{model}', compute_type='int8')
        segs,info=m.transcribe(r"{audio_path}", beam_size=1, vad_filter=True)
        txt=' '.join((s.text or '').strip() for s in segs).strip()
        print(txt)
        '''
    )
    p = run([str(VENV_PY), '-c', script])
    return p.stdout.strip()


def summarize_with_ollama(title: str, channel: str, transcript: str):
    prompt = f'''Du är en analytiker för FitzWorks.

Video: {title}
Kanal: {channel}

Transkribering:
{transcript[:22000]}

Gör en KORT svensk rapport med exakt dessa rubriker:
1) TLDR (3 meningar)
2) Viktiga idéer (max 5 bullets)
3) Applicering i FitzWorks (max 5 konkreta actions)
4) Vad vi INTE ska göra (max 3 risker)
5) Applicerbar nu? (JA/NEJ + 1 mening varför)
6) Rekommenderat nästa steg (1 sak idag)
'''
    p = run(['ollama', 'run', 'qwen3:8b-16k'], input_text=prompt, check=False)
    if p.returncode != 0 or not p.stdout.strip():
        return 'Ollama-summering misslyckades. Transkript sparat för manuell analys.'
    return p.stdout.strip()


def classify_now_or_later(analysis: str) -> str:
    m = re.search(r'Applicerbar nu\?\s*\(?\s*(JA|NEJ)', analysis, re.IGNORECASE)
    if m:
        return 'NOW' if m.group(1).upper() == 'JA' else 'BANK'
    return 'BANK'


def infer_categories(title: str, channel: str, analysis: str) -> str:
    blob = f"{title} {channel} {analysis}".lower()
    cats = []
    if any(x in blob for x in ['ai', 'artificiell', 'openai', 'anthropic']): cats.append('AI')
    if any(x in blob for x in ['aktie', 'stocks', 'invest', 'portfolio', 'market']): cats.append('Investering')
    if any(x in blob for x in ['risk', 'bubble', 'krasch', 'crash']): cats.append('Risk')
    if any(x in blob for x in ['energy', 'energi', 'nuclear', 'data center', 'infrastruktur']): cats.append('Infrastruktur')
    if any(x in blob for x in ['automation', 'produktiv', 'workflow', 'process']): cats.append('Automation')
    if 'comparative advantage' in blob or 'komparativ' in blob: cats.append('Comparative advantage')
    if not cats: cats = ['Övrigt']
    return ', '.join(dict.fromkeys(cats))


def append_bank_entry(title: str, url: str, channel: str, out_path: pathlib.Path, analysis: str):
    bank = OUTDIR / 'BANK.md'
    if not bank.exists():
        bank.write_text('# YouTube Knowledge Bank (FitzWorks)\n\n| Datum | Titel | Kanal | Kategorier | Status | Länk | Notes |\n|---|---|---|---|---|---|---|\n', encoding='utf-8')
    status = classify_now_or_later(analysis)
    note = 'Direkt kandidat' if status == 'NOW' else 'Spara för senare'
    categories = infer_categories(title, channel, analysis).replace('|','/')
    row = f"| {dt.datetime.now().astimezone().strftime('%Y-%m-%d')} | {title.replace('|','/')} | {channel.replace('|','/')} | {categories} | {status} | [{out_path.name}]({out_path.name}) | {note} |\n"
    with bank.open('a', encoding='utf-8') as f:
        f.write(row)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('url')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--model', default='base')
    args = ap.parse_args()

    OUTDIR.mkdir(parents=True, exist_ok=True)

    meta = get_meta(args.url)
    vid = meta.get('id', 'video')
    title = meta.get('title', 'Untitled')
    channel = meta.get('channel') or meta.get('uploader') or 'Unknown'
    duration = meta.get('duration')

    ts = dt.datetime.now().astimezone().strftime('%Y-%m-%d_%H%M')
    slug = sanitize(title)
    out_path = OUTDIR / f'{ts}_{slug}_{vid}.md'

    transcript = ''
    analysis = ''

    if args.dry_run:
      analysis = 'DRY RUN: metadata ok, skippade download/transkribering.'
    else:
      audio = download_audio(args.url, vid)
      transcript = transcribe(audio, model=args.model)
      analysis = summarize_with_ollama(title, channel, transcript)

    md = f"""# YouTube Analysis — {title}

- URL: {args.url}
- Kanal: {channel}
- Duration: {duration}
- Video ID: {vid}
- Timestamp: {dt.datetime.now().astimezone().isoformat()}

## FitzWorks Analysis
{analysis}

## Transcript
{transcript if transcript else '(none)'}
"""
    out_path.write_text(md, encoding='utf-8')
    append_bank_entry(title, args.url, channel, out_path, analysis)
    print(str(out_path))


if __name__ == '__main__':
    main()
