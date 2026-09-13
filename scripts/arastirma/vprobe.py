import json, re, time, urllib.parse, sys
import requests

BASE="https://dys.logo.cloud"
Q={"cid":"c374d466-272d-4dda-bb15-21910df7fa69","link":"2d55d104-9ff0-4620-aa45-5f004cc5f31d",
   "tenantId":"cdd87e13-3009-4dd1-a5b8-2a005c0e58da","hideName":"True"}
page_url=BASE+"/external?"+urllib.parse.urlencode(Q)

s=requests.Session()
s.headers["User-Agent"]="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128 Safari/537.36"
r=s.get(page_url, timeout=60)
print("bootstrap", r.status_code, len(r.text))
appid=re.search(r'vaadin\.initApplication\("([^"]+)"', r.text).group(1)
cfg=json.loads(re.search(r'vaadin\.initApplication\("[^"]+",(\{.*?\})\);', r.text, re.S).group(1))
print("appId", appid, "serviceUrl", cfg.get("serviceUrl"))

now=int(time.time()*1000)
params=[("v-browserDetails","1"),("theme",cfg.get("theme","")),("v-appId",appid),
        ("v-sh","1080"),("v-sw","1920"),("v-cw","1600"),("v-ch","900"),
        ("v-curdate",str(now)),("v-tzo","-180"),("v-dstd","0"),("v-rtzo","-180"),
        ("v-dston","false"),("v-tzid","Europe/Istanbul"),("v-vw","1600"),("v-vh","900"),
        ("v-loc",page_url),("v-wn",appid+"-0.1")]
post_url=page_url+"&v-"+str(now)
r2=s.post(post_url, data=params, headers={"Content-Type":"application/x-www-form-urlencoded"}, timeout=60)
print("init POST", r2.status_code, r2.headers.get("content-type"), len(r2.text))
open("init.json","w").write(r2.text)
print(r2.text[:1500])

import re as _re
u=json.loads(r2.text if False else open('init.json').read())
uidl=json.loads(json.loads(open('init.json').read())['uidl'])
stream=None
for k,v in uidl['state'].items():
    res=v.get('resources',{})
    if 'source' in res:
        stream=res['source']['uRL']
print("STREAM URL:", stream)
r3=s.get(stream, timeout=90, allow_redirects=True)
print("stream", r3.status_code, r3.headers.get('content-type'), r3.headers.get('content-disposition'), len(r3.content))
open('stream1.bin','wb').write(r3.content)
