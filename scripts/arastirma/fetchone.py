import json, re, time, sys, urllib.parse, requests
BASE="https://dys.logo.cloud"
def fetch(doc_url, skip_bootstrap=False):
    s=requests.Session()
    s.headers["User-Agent"]="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128 Safari/537.36"
    page_url=BASE+"/"+doc_url
    info={}
    if skip_bootstrap:
        appid="ROOT-2521314"; theme="documentservice"
    else:
        r=s.get(page_url, timeout=60); info['boot']=r.status_code
        m=re.search(r'vaadin\.initApplication\("([^"]+)",(\{.*?\})\);', r.text, re.S)
        if not m: return {'err':'no-bootstrap','status':r.status_code,'body':r.text[:300]}
        appid=m.group(1); theme=json.loads(m.group(2)).get('theme','')
    now=int(time.time()*1000)
    params=[("v-browserDetails","1"),("theme",theme),("v-appId",appid),("v-sh","1080"),("v-sw","1920"),
            ("v-cw","1600"),("v-ch","900"),("v-curdate",str(now)),("v-tzo","-180"),("v-dstd","0"),
            ("v-rtzo","-180"),("v-dston","false"),("v-tzid","Europe/Istanbul"),("v-vw","1600"),
            ("v-vh","900"),("v-loc",page_url),("v-wn",appid+"-0.1")]
    sep="&" if "?" in page_url else "?"
    r2=s.post(page_url+sep+"v-"+str(now), data=params,
              headers={"Content-Type":"application/x-www-form-urlencoded"}, timeout=60)
    info['init']=r2.status_code
    try: uidl=json.loads(json.loads(r2.text)['uidl'])
    except Exception as e: return {**info,'err':'uidl-parse: '+str(e),'body':r2.text[:400]}
    urls=[]; ids=[]
    for k,v in uidl.get('state',{}).items():
        ids.append(v.get('id'))
        for rk,rv in (v.get('resources') or {}).items():
            urls.append((v.get('id'), rk, rv.get('uRL')))
    info['componentIds']=ids; info['resources']=urls
    if not urls: return {**info,'err':'no-resource'}
    src=[u for i,k,u in urls if k=='source'] or [u for _,_,u in urls]
    r3=s.get(src[0], timeout=120)
    info['stream']=r3.status_code
    info['ctype']=r3.headers.get('content-type')
    info['cdisp']=r3.headers.get('content-disposition')
    info['bytes']=len(r3.content)
    info['head']=r3.content[:200]
    return info

if __name__=='__main__':
    for a in sys.argv[1:]:
        print('###', a[:70]); print(json.dumps(fetch(a), ensure_ascii=False, default=str, indent=1)[:1500]); print()
