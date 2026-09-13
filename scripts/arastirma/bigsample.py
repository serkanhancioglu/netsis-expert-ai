import json, re, time, random, os, requests, concurrent.futures as cf
BASE="https://dys.logo.cloud"; UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/128 Safari/537.36"
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
    return s.get(src,timeout=240)
flat=json.load(open('flat_tree.json'))
random.seed(99)
pool=[x for x in flat if x['leaf']]
folders=[x for x in flat if not x['leaf']]
sample=random.sample(pool,44)+random.sample(folders,6)
os.makedirs('samples2',exist_ok=True)
def job(a):
    i,x=a
    try:
        r=fetch(x['doc_url']); open(f"samples2/{i:03d}.html","wb").write(r.content)
        return (i,r.status_code,len(r.content),x['path'][-1])
    except Exception as e: return (i,'ERR',str(e)[:80],x['path'][-1])
with cf.ThreadPoolExecutor(max_workers=4) as ex:
    for res in ex.map(job, list(enumerate(sample))): print(res, flush=True)
json.dump(sample, open('sample2.json','w'), ensure_ascii=False, indent=1)
