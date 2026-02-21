#!/usr/bin/env python3
import json, re, datetime
from pathlib import Path

ROOT = Path('/Users/bob/.openclaw/workspace')
INBOUND = Path('/Users/bob/.openclaw/media/inbound')
INBOX = ROOT / 'VOICE_INBOX.md'
STATE = ROOT / 'memory' / 'voice_ingest_state.json'
STATE.parent.mkdir(parents=True, exist_ok=True)

AUDIO_EXT = {'.ogg', '.oga', '.opus', '.mp3', '.m4a', '.wav', '.aac', '.webm'}


def load_state():
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding='utf-8'))
        except Exception:
            pass
    return {"processed": []}


def save_state(st):
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding='utf-8')


def append_inbox(entry):
    if not INBOX.exists():
        INBOX.write_text('# Voice Inbox\n\n---\n', encoding='utf-8')
    with INBOX.open('a', encoding='utf-8') as f:
        f.write(f"\n### {entry['id']}\n")
        f.write(f"- id: {entry['id']}\n")
        f.write(f"- date: {entry['date']}\n")
        f.write(f"- source: telegram voice\n")
        f.write(f"- transcript: {entry['transcript']}\n")
        f.write(f"- tags: [reference]\n")
        f.write(f"- status: new\n")
        f.write(f"- next_action: Klassificera och flytta till rätt spår\n")


def clean_text(text):
    t = re.sub(r'\s+', ' ', text or '').strip()
    return t[:3000] if t else '(tom transkribering)'


def main():
    try:
        from faster_whisper import WhisperModel
    except Exception as e:
        print(f'error_import_faster_whisper:{e}')
        return 1

    st = load_state()
    processed = set(st.get('processed', []))

    files = []
    if INBOUND.exists():
        for p in INBOUND.iterdir():
            if p.suffix.lower() in AUDIO_EXT:
                files.append(p)
    files.sort(key=lambda x: x.stat().st_mtime)

    if not files:
        print('no_audio_files')
        return 0

    model = WhisperModel('tiny', device='cpu', compute_type='int8')

    added = 0
    for fp in files:
        key = str(fp)
        if key in processed:
            continue
        try:
            segments, info = model.transcribe(str(fp), beam_size=1, vad_filter=True)
            text = ' '.join(seg.text for seg in segments)
            text = clean_text(text)
        except Exception as e:
            text = f'(transkribering misslyckades: {e})'

        entry = {
            'id': fp.name,
            'date': datetime.datetime.now().astimezone().isoformat(),
            'transcript': text,
        }
        append_inbox(entry)
        processed.add(key)
        added += 1

    st['processed'] = sorted(processed)
    save_state(st)
    print(f'transcribed_added:{added}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
