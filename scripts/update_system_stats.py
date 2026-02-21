#!/usr/bin/env python3
import json, re, subprocess, datetime, os

def sh(cmd):
    return subprocess.check_output(cmd, shell=True, text=True, executable='/bin/zsh').strip()

def safe(cmd, default=''):
    try:
        return sh(cmd)
    except Exception:
        return default

now = datetime.datetime.now(datetime.timezone.utc).astimezone()

# CPU
cpu_line = safe("/usr/bin/top -l 1 | /usr/bin/grep 'CPU usage'")
m = re.search(r"([0-9.]+)% user,\s*([0-9.]+)% sys,\s*([0-9.]+)% idle", cpu_line)
cpu_used = round(100.0 - float(m.group(3)), 1) if m else None

# RAM
memsize = int(safe("/usr/sbin/sysctl -n hw.memsize", "0") or 0)
vm = safe("/usr/bin/vm_stat", "")
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
parts = re.split(r"\s+", safe("/bin/df -H / | /usr/bin/tail -1", ""))
size = parts[1] if len(parts) > 1 else "-"
used = parts[2] if len(parts) > 2 else "-"
avail = parts[3] if len(parts) > 3 else "-"
cap = parts[4].replace('%','') if len(parts) > 4 else "-"

# Temperature / thermal
therm = safe("/usr/bin/pmset -g therm 2>/dev/null", "")
thermal_status = "Normal"
if "CPU_Speed_Limit" in therm or "GPU_Speed_Limit" in therm:
    thermal_status = "Constrained"
elif "No thermal warning" in therm:
    thermal_status = "Normal"
elif therm.strip():
    thermal_status = "Check"

temp_c = None  # macOS may not expose direct CPU temp without elevated permissions/tools.

# Network
iface = "en0"
route = safe("/usr/sbin/route -n get default 2>/dev/null | /usr/bin/grep interface:", "")
mi = re.search(r"interface:\s*(\S+)", route)
if mi:
    iface = mi.group(1)

net = safe(f"/usr/sbin/netstat -ibn | /usr/bin/grep '^{iface}\\b'", "")
ibytes = obytes = None
if net:
    best_i = best_o = 0
    for line in net.splitlines():
        cols = re.split(r"\s+", line.strip())
        if len(cols) >= 10:
            try:
                # netstat -ibn columns:
                # Name Mtu Network Address Ipkts Ierrs Ibytes Opkts Oerrs Obytes Coll
                i = int(cols[6]); o = int(cols[9])
                if i > best_i: best_i = i
                if o > best_o: best_o = o
            except Exception:
                pass
    ibytes, obytes = best_i, best_o

prev_path = 'system_stats_prev.json'
rx_kbps = tx_kbps = None
if os.path.exists(prev_path):
    try:
        prev = json.load(open(prev_path, 'r', encoding='utf-8'))
        if prev.get('network', {}).get('interface') == iface and ibytes is not None and obytes is not None:
            prev_i = prev['network'].get('rx_bytes_total')
            prev_o = prev['network'].get('tx_bytes_total')
            prev_t = datetime.datetime.fromisoformat(prev['updated_at'])
            dt = max((now - prev_t).total_seconds(), 1.0)
            if isinstance(prev_i, int) and ibytes >= prev_i:
                rx_kbps = round((ibytes - prev_i) / 1024.0 / dt, 1)
            if isinstance(prev_o, int) and obytes >= prev_o:
                tx_kbps = round((obytes - prev_o) / 1024.0 / dt, 1)
    except Exception:
        pass

data = {
  "updated_at": now.isoformat(),
  "cpu": {"used_percent": cpu_used},
  "ram": {"used_percent": ram_used_pct},
  "disk": {"size": size, "used": used, "avail": avail, "used_percent": float(cap) if cap != '-' else None},
  "temperature": {"cpu_c": temp_c, "thermal_status": thermal_status},
  "network": {
    "interface": iface,
    "rx_bytes_total": ibytes,
    "tx_bytes_total": obytes,
    "rx_kbps": rx_kbps,
    "tx_kbps": tx_kbps
  }
}

with open('system_stats.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
with open(prev_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('updated system_stats.json')
