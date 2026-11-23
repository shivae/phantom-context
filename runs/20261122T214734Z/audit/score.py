import json,sys,collections
d=sys.argv[1]
km=json.load(open(f"{d}/keymap.json"))
res=json.load(open(f"{d}/labels.json"))
lab={}
for b in res:
    for x in b["labels"] or []: lab[x["key"]]=x
missing=[k for k in km if k not in lab]
print("labelled",len(lab),"missing",len(missing),"unknown",len(set(lab)-set(km)))
models=["qwen2.5-1.5b","qwen2.5-7b","qwen3-8b","granite-3.3-8b"]
print("\n| model | truth | kept outcome | inverted | in progress | dropped | low-confidence | judge agrees | n |")
print("|---|---|---:|---:|---:|---:|---:|---:|---:|")
for m in models:
    for o in ("fail","success"):
        ks=[k for k,v in km.items() if v["model"]==m and v["outcome"]==o and k in lab]
        c=collections.Counter(lab[k]["label"] for k in ks)
        keep="FAILED" if o=="fail" else "DONE"; inv="DONE" if o=="fail" else "FAILED"
        n=len(ks); f=lambda x:f"{x/n:.0%} ({x})"
        agree=sum(km[k]["judge"]==lab[k]["label"] or (km[k]["judge"]=="OTHER" and lab[k]["label"]=="NOT_MENTIONED") for k in ks)
        print(f"| {m} | {o} | {f(c[keep])} | {f(c[inv])} | {f(c['IN_PROGRESS'])} | {f(c['NOT_MENTIONED'])} | {sum(not lab[k]['confident'] for k in ks)} | {agree/n:.0%} | {n} |")
print("\nInverted failures (truth=fail, summary says DONE):")
for k,v in km.items():
    if k in lab and v["outcome"]=="fail" and lab[k]["label"]=="DONE":
        print(f"  {v['model']} {v['scn']} {v['crit']} judge={v['judge']} conf={lab[k]['confident']}: {lab[k]['quote'][:160]}")
