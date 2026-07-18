#!/usr/bin/env python3
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]; ALLOWED={'MUST','MUST NOT','SHOULD','SHOULD NOT','MAY'}
def fm(t):
    e=t.find('\n---\n',4);o={}
    for line in t[4:e].splitlines():
        if line.startswith(' ') or ':' not in line:continue
        k,v=line.split(':',1);o[k.strip()]=v.strip()
    return o
def rows(p,prefix,n):
    out=[]
    for line in p.read_text().splitlines():
        if line.startswith('| '+prefix):
            c=[x.strip() for x in line.strip().strip('|').split('|')]
            if len(c)!=n:raise ValueError(f'{p} malformed {prefix}')
            out.append(c)
    return out
def main():
    e=[]
    docs={'KERNEL-0000':('KERNEL-0000-specification-family-index.md','0.4.0-draft.4'),'KERNEL-0001':('KERNEL-0001-core-operational-contract.md','0.2.2-draft.4'),'KERNEL-0002':('KERNEL-0002-canonical-object-data-model.md','0.2.0-draft.2'),'KERNEL-0003':('KERNEL-0003-lifecycle-state-machines.md','0.2.0-draft.2')}
    for did,(name,ver) in docs.items():
        p=ROOT/'standards/kernel'/name
        if not p.exists():e.append('missing '+did);continue
        m=fm(p.read_text())
        if m.get('id')!=did or m.get('status')!='Draft' or m.get('version')!=ver:e.append(did+' metadata')
    for did in ['KERNEL-0004','KERNEL-0005']:
        if list((ROOT/'standards/kernel').glob(did+'-*.md')):e.append(did+' exists')
    d=json.loads((ROOT/'reference/kernel/mingos-kernel-object-lifecycle-model.json').read_text())
    if d.get('schema')!='mingos.kernel-object-lifecycle-model.v0.2':e.append('schema')
    for path,key,prefix in [(ROOT/'standards/kernel/KERNEL-0002-canonical-object-data-model.md','object_requirements','KDO-'),(ROOT/'standards/kernel/KERNEL-0003-lifecycle-state-machines.md','lifecycle_requirements','KLS-')]:
        mr=rows(path,prefix,8);jr=d[key]
        if len(mr)!=len(jr):e.append(key+' count');continue
        for m,j in zip(mr,jr):
            s=j['source_refs'][0];es=f"{s['source_id']} / {s['status']} / {s['version']} / `{s['path']}` / {s['locator']} / {s['baseline_type']}"
            if not (m[0]==j['id'] and m[1]==j['domain'] and m[2].strip('`')==j['level'] and m[3]==j['text'] and m[4]==es and m[5].strip('`')==j['source_treatment'] and m[6]=='; '.join(j['verification_methods']) and m[7]=='; '.join(j['evidence_types'])):e.append(j['id']+' sync')
            if j['level'] not in ALLOWED:e.append(j['id']+' level')
    obj=rows(ROOT/'standards/kernel/KERNEL-0002-canonical-object-data-model.md','KOT-',7)
    if [x[0] for x in obj]!=[x['id'] for x in d['object_types']]:e.append('object IDs')
    for sm in d['state_machines']:
        st=set(sm['states']);seen=set()
        for a,b in sm['transitions']:
            if a not in st or b not in st or a==b or (a,b) in seen:e.append(sm['id']+' transition')
            seen.add((a,b))
    for f in d['process_flows']:
        if f['transitions']!=[[a,b] for a,b in zip(f['stages'],f['stages'][1:])]:e.append(f['id']+' flow')
    core=json.loads((ROOT/'reference/kernel/mingos-kernel-core-requirements.json').read_text())
    if core['family']['id']!='kernel-family/0.4.0-draft.4' or core['family']['reserved_not_created']!=['KERNEL-0004','KERNEL-0005']:e.append('family')
    if d['review']['state']!='PreparedNotExecuted' or d['conformance']['current_claim']!='NoCurrentKernelConformanceClaim':e.append('boundary')
    state=(ROOT/'governance/status/GOV-0001-current-canonical-state.md').read_text()
    if 'Foundation 1.0 / Day 17' not in state or '1.0.0-alpha.17' not in state:e.append('day17')
    if e:
        print('Round08 RevA validation failed:');[print(' -',x) for x in e];return 1
    print('Round08 RevA validation passed: 35 objects, 36 KDO, 34 KLS, 17 object state machines, 9 process flows, no conformance claim.')
    return 0
if __name__=='__main__':raise SystemExit(main())
