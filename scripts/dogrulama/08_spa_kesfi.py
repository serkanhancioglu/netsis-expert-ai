#!/usr/bin/env python3
"""Portalin Angular uygulamasini tersine cevirip uc adresi bulur.

Protokolun nasil bulundugunu tekrarlanabilir kilar. Site yeniden yayinlanirsa
(paket adlari degisir) bu betik yeni adresleri kendisi bulur.

Adimlar:
  1. Kabuk HTML'i indir, runtime/main/chunk paket adlarini cikar
  2. Tembel yuklenen butun chunk'lari indir
  3. Yapilandirma adresini (/assets/config/app.config.json) bul ve indir
  4. DYS_APP_URL ve CONFIG.TOKEN.API_URI degerlerini yazdir
  5. Paketlerdeki /api/... uc noktalarini listele

Kullanim:
    python 08_spa_kesfi.py [PORTAL_ADRESI]
"""
import json
import re
import sys
import tempfile
from pathlib import Path

import requests

DEFAULT_PORTAL = "https://polaris.logo.cloud"
UA = "netsis-spa-kesfi/1.0 (dogrulama betigi)"


def main(portal: str = DEFAULT_PORTAL) -> int:
    session = requests.Session(); session.headers["User-Agent"] = UA
    workdir = Path(tempfile.mkdtemp())
    print(f"calisma klasoru: {workdir}\n")

    index = session.get(portal, timeout=60).text
    bundles = re.findall(r'src="([^"]+\.js[^"]*)"', index)
    print("1) kabuk HTML'deki paketler:")
    for b in bundles:
        print("   ", b)

    runtime = next((b for b in bundles if "runtime" in b), None)
    chunk_names: list[str] = []
    if runtime:
        text = session.get(f"{portal}/{runtime.lstrip('/')}", timeout=60).text
        mapping = dict(re.findall(r'(\d+):"([a-f0-9]{16,32})"', text))
        aliases = dict(re.findall(r'\{(\d+):"([a-z]+)"\}', text))
        for number, digest in mapping.items():
            chunk_names.append(f"{aliases.get(number, number)}.{digest}.js")
        print(f"\n2) tembel chunk sayisi: {len(chunk_names)}")

    sources = {}
    for name in [b.lstrip("/") for b in bundles] + chunk_names:
        try:
            body = session.get(f"{portal}/{name.split('?')[0]}", timeout=90).text
        except requests.RequestException:
            continue
        sources[name] = body

    joined = "\n".join(sources.values())
    config_urls = sorted(set(re.findall(r'configUrl:"([^"]+)"', joined)))
    print(f"\n3) yapilandirma adresi: {config_urls or '(bulunamadi)'}")

    for config_url in config_urls:
        response = session.get(f"{portal}{config_url}", timeout=90)
        if response.status_code != 200:
            print(f"   {config_url} -> {response.status_code}")
            continue
        config = response.json()
        print(f"\n4) {config_url} icindeki adresler:")
        print(f"   DYS_APP_URL        = {config.get('DYS_APP_URL')}")
        token = (config.get("CONFIG") or {}).get("TOKEN") or {}
        print(f"   CONFIG.TOKEN.API_URI = {token.get('API_URI')}")
        print(f"   CHATBOT_URL        = {config.get('CHATBOT_URL')}")

    endpoints = sorted(set(re.findall(r'"(/api/[A-Za-z0-9/_.-]+)"', joined)))
    print(f"\n5) paketlerdeki API uc noktalari ({len(endpoints)}):")
    for endpoint in endpoints:
        print("   ", endpoint)

    print("\nBEKLENEN SONUC:")
    print("   DYS_APP_URL          -> https://dys.logo.cloud")
    print("   CONFIG.TOKEN.API_URI -> https://polaris.logo.com.tr")
    print("   /api/Documents/GetAuthorizedTrees  (hiyerarsi agaci)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PORTAL))
