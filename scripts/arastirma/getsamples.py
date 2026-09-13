import json, re, time, os, requests
BASE="https://dys.logo.cloud"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128 Safari/537.36"
def fetch(doc_url):
    s=requests.Session(); s.headers["User-Agent"]=UA
    page=BASE+"/"+doc_url
    r=s.get(page,timeout=60)
    m=re.search(r'vaadin\.initApplication\("([^"]+)",(\{.*?\})\);', r.text, re.S)
    appid=m.group(1); theme=json.loads(m.group(2)).get('theme','')
    now=int(time.time()*1000)
    p=[("v-browserDetails","1"),("theme",theme),("v-appId",appid),("v-sh","1080"),("v-sw","1920"),
       ("v-cw","1600"),("v-ch","900"),("v-curdate",str(now)),("v-tzo","-180"),("v-dstd","0"),
       ("v-rtzo","-180"),("v-dston","false"),("v-tzid","Europe/Istanbul"),("v-vw","1600"),
       ("v-vh","900"),("v-loc",page),("v-wn",appid+"-0.1")]
    r2=s.post(page+"&v-"+str(now),data=p,headers={"Content-Type":"application/x-www-form-urlencoded"},timeout=60)
    uidl=json.loads(json.loads(r2.text)['uidl'])
    src=None
    for k,v in uidl['state'].items():
        rr=(v.get('resources') or {}).get('source')
        if rr: src=rr['uRL']
    r3=s.get(src,timeout=180)
    return r3
sample=json.load(open('sample.json'))
for i,x in enumerate(sample):
    try:
        r=fetch(x['doc_url'])
        fn=f"samples/{i:02d}.html"
        open(fn,'wb').write(r.content)
        print(i, r.status_code, r.headers.get('content-type'), len(r.content), '|', x['path'][-1])
    except Exception as e:
        print(i,'ERR',e)
    time.sleep(1.0)
