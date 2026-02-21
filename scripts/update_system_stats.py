#!/usr/bin/env python3
import json, re, subprocess, datetime

def sh(cmd):
    return subprocess.check_output(cmd, shell=True, text=True, executable='/bin/zsh').strip()

# CPU
cpu_line = sh("/usr/bin/top -l 1 | /usr/bin/grep 'CPU usage'")
m = re.search(r"([0-9.]+)% user,\s*([0-9.]+)% sys,\s*([0-9.]+)% idle", cpu_line)
cpu_used = round(100.0 - float(m.group(3)), 1) if m else None

# RAM
try:
    memsize = int(sh("/usr/sbin/sysctl -n hw.memsize"))
except Exception:
    memsize = 0
vm = sh("/usr/bin/vm_stat")
page_size = 4096
mps = re.search(r"page size of (\d+) bytes", vm)
if mps:
    page_size = int(mps.group(1))

def pages(name):
    mm = re.search(rf"{re.escape(name)}:\s+([0-9.]+)", vm)
    return int(float(mm.group(1))) if mm else 0

used_pages = pages("Pages wired down") + pages("Pages active") + pages("Pages occupied by compressor")
used_bytes = used_pages * page_size
ram_used_pct = round((used_bytes / memsize) * 100, 1) if memsize else None

# Disk
df = sh("/bin/df -H / | /usr/bin/tail -1")
parts = re.split(r"\s+", df)
size = parts[1] if len(parts) > 1 else "-"
used = parts[2] if len(parts) > 2 else "-"
avail = parts[3] if len(parts) > 3 else "-"
cap = parts[4].replace('%','') if len(parts) > 4 else "-"

data = {
  "updated_at": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(),
  "cpu": {"used_percent": cpu_used},
  "ram": {"used_percent": ram_used_pct},
  "disk": {"size": size, "used": used, "avail": avail, "used_percent": float(cap) if cap!='-' else None}
}

with open("system_stats.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("updated system_stats.json")
