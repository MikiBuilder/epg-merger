import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime, timezone

SOURCES = [
    "https://raw.githubusercontent.com/davidmuma/EPG_dobleM/refs/heads/master/guiaiptv.xml",
    "https://raw.githubusercontent.com/matthuisman/i.mjh.nz/refs/heads/master/PlutoTV/all.xml",
    "https://raw.githubusercontent.com/matthuisman/i.mjh.nz/refs/heads/master/SamsungTVPlus/es.xml",
    "https://raw.githubusercontent.com/matthuisman/i.mjh.nz/refs/heads/master/Plex/es.xml",
]

OUTPUT_XML  = "merged.xml"
OUTPUT_LIST = "channels.txt"


def fetch_xml(url):
    try:
        r = requests.get(url, timeout=60, headers={"User-Agent": "EPG-Merger/1.0"})
        r.raise_for_status()
        root = ET.fromstring(r.content)
        print(f"  ✓  {url}")
        return root
    except Exception as e:
        print(f"  ✗  {url}  →  {e}")
        return None


def merge():
    print(f"\n[{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC]  Iniciando merge EPG...\n")

    channels   = {}
    programmes = []

    for url in SOURCES:
        root = fetch_xml(url)
        if root is None:
            continue
        for ch in root.findall("channel"):
            cid = ch.get("id", "").strip()
            if cid and cid not in channels:
                channels[cid] = ch
        for prog in root.findall("programme"):
            programmes.append(prog)

    # ── Build output tree ──────────────────────────────────────────
    tv = ET.Element("tv")
    tv.set("generator-info-name", "epg-merger")
    tv.set("generated-at", datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S +0000"))

    for ch in channels.values():
        tv.append(ch)
    for prog in programmes:
        tv.append(prog)

    xml_str = minidom.parseString(ET.tostring(tv, encoding="unicode")).toprettyxml(indent="  ")
    clean = "\n".join(xml_str.splitlines())

    with open(OUTPUT_XML, "w", encoding="utf-8") as f:
        f.write(clean)

    # ── Channel list ───────────────────────────────────────────────
    sorted_channels = sorted(channels.keys())
    total = len(sorted_channels)

    with open(OUTPUT_LIST, "w", encoding="utf-8") as f:
        f.write(f"Total canales: {total} canales\n")
        f.write("=" * 40 + "\n")
        for cid in sorted_channels:
            ch_el = channels[cid]
            display = ch_el.findtext("display-name") or cid
            f.write(f"{display}  [{cid}]\n")

    print(f"\n✅  merged.xml     →  {total} canales,  {len(programmes)} programas")
    print(f"✅  channels.txt   →  lista de canales generada")


if __name__ == "__main__":
    merge()
