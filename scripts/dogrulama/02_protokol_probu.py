#!/usr/bin/env python3
"""Vaadin protokolunun varsayimlarini canli olarak dogrular.

Bu betik, kazima aracinin dayandigi dort iddiayi tek tek sinar:

  A. Tek bir oturum birden fazla dokumana hizmet edebiliyor mu
  B. Onyukleme atlanabiliyor mu (dokuman basina 3 degil 2 istek)
  C. Uygulama kimligi (appId) oturumlar arasinda sabit mi
  D. Gecersiz bir baglantida sunucu ne donuyor

D onemli: gecersiz baglantida UIDL, icerik yerine bir uyari ikonu
(theme://images/task_list_warning.svg) dondurur. "Ilk kaynagi indir" diyen
naif bir kod o ikonu indirmeye calisir.

SITEYI YORMAMAK ICIN: az sayida istek atar, aralarinda bekler.
"""
import json
import re
import sys
import time

import requests

BASE = "https://dys.logo.cloud"
UA = "netsis-protokol-probu/1.0 (dogrulama betigi)"


def init_post(session, page_url, app_id, theme):
    stamp = int(time.time() * 1000)
    payload = [
        ("v-browserDetails", "1"), ("theme", theme), ("v-appId", app_id),
        ("v-sh", "1080"), ("v-sw", "1920"), ("v-cw", "1600"), ("v-ch", "900"),
        ("v-curdate", str(stamp)), ("v-tzo", "-180"), ("v-dstd", "0"),
        ("v-rtzo", "-180"), ("v-dston", "false"), ("v-tzid", "Europe/Istanbul"),
        ("v-vw", "1600"), ("v-vh", "900"), ("v-loc", page_url),
        ("v-wn", f"{app_id}-0.1"),
    ]
    separator = "&" if "?" in page_url else "?"
    return session.post(
        f"{page_url}{separator}v-{stamp}", data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=60,
    )


def bootstrap(session, doc_url):
    response = session.get(f"{BASE}/{doc_url}", timeout=60)
    match = re.search(r'vaadin\.initApplication\("([^"]+)",(\{.*?\})\);', response.text, re.S)
    if not match:
        return None, None
    return match.group(1), json.loads(match.group(2)).get("theme", "")


def stream_urls(uidl):
    found = []
    for value in (uidl.get("state") or {}).values():
        if not isinstance(value, dict):
            continue
        for resource in (value.get("resources") or {}).values():
            if isinstance(resource, dict) and resource.get("uRL"):
                found.append((value.get("id"), resource["uRL"]))
    return found


def main(doc_urls):
    if not doc_urls:
        sys.exit("Kullanim: python 02_protokol_probu.py '<doc_url>' ['<doc_url>' ...]\n"
                 "doc_url ornegi: external?cid=...&link=...&tenantId=...&hideName=True")

    print("=== A) Tek oturum, birden fazla dokuman ===")
    session = requests.Session(); session.headers["User-Agent"] = UA
    app_id, theme = bootstrap(session, doc_urls[0])
    print(f"  onyukleme bir kez: appId={app_id} theme={theme}")
    for doc_url in doc_urls:
        response = init_post(session, f"{BASE}/{doc_url}", app_id, theme)
        try:
            uidl = json.loads(json.loads(response.text)["uidl"])
            found = stream_urls(uidl)
            print(f"  init={response.status_code} kaynak={found[0][0] if found else None}")
        except Exception as exc:
            print(f"  init={response.status_code} COZULEMEDI: {exc}")
        time.sleep(1.0)

    print("\n=== B) Onyukleme atlanabiliyor mu ===")
    fresh = requests.Session(); fresh.headers["User-Agent"] = UA
    response = init_post(fresh, f"{BASE}/{doc_urls[0]}", "ROOT-2521314", "documentservice")
    ok = "json" in (response.headers.get("Content-Type") or "").lower()
    print(f"  taze oturum + sabit appId -> {response.status_code}, JSON mu: {ok}")
    time.sleep(1.0)

    print("\n=== C) appId oturumlar arasinda sabit mi ===")
    ids = []
    for doc_url in doc_urls[:3]:
        s = requests.Session(); s.headers["User-Agent"] = UA
        ids.append(bootstrap(s, doc_url)[0])
        time.sleep(0.8)
    print(f"  {ids} -> {'sabit' if len(set(ids)) == 1 else 'DEGISKEN'}")

    print("\n=== D) Gecersiz baglantida ne donuyor ===")
    zero = "00000000-0000-0000-0000-000000000000"
    bad = f"external?cid={zero}&link={zero}&tenantId={zero}&hideName=True"
    s = requests.Session(); s.headers["User-Agent"] = UA
    app_id, theme = bootstrap(s, bad)
    if app_id:
        response = init_post(s, f"{BASE}/{bad}", app_id, theme)
        uidl = json.loads(json.loads(response.text)["uidl"])
        keys = list((uidl.get("state") or {}).keys())
        print(f"  durum anahtarlari: {keys}")
        print(f"  kaynaklar: {stream_urls(uidl)}")
        print("  -> 'expired' iceren bir anahtar ve theme:// semali kaynak bekleniyor")


if __name__ == "__main__":
    main(sys.argv[1:])
