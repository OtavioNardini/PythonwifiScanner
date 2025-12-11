import subprocess
import re

def scan_wifi_windows():
    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            encoding="latin-1"
        )
    except Exception as e:
        return {"error": str(e)}

    networks = []
    blocks = output.split("SSID ")

    for block in blocks[1:]:
        try:
            ssid = block.split(":")[1].split("\n")[0].strip()
            ssid_block = block.split("BSSID")[0]

            signal = re.search(r"Signal\s*:\s*(\d+)%", ssid_block)
            channel = re.search(r"Channel\s*:\s*(\d+)", ssid_block)

            networks.append({
                "ssid": ssid,
                "signal": signal.group(1) if signal else None,
                "channel": channel.group(1) if channel else None,
            })
        except:
            pass

    return networks
