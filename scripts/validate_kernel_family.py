#!/usr/bin/env python3
"""Validate Round 08 Kernel core, object model, lifecycles, and source baselines."""
from pathlib import Path
import json,re,subprocess
ROOT=Path(__file__).resolve().parents[1]
K1=ROOT/"standards/kernel/KERNEL-0001-core-operational-contract.md"
CORE=ROOT/"reference/kernel/mingos-kernel-core-requirements.json"
A1=ROOT/"reference/kernel/REF-0032-kernel-core-ambiguity-register.md"
V=ROOT/"reference/kernel/REF-0034-kernel-core-vocabulary-status-map.md"
MODEL=ROOT/"reference/kernel/mingos-kernel-object-lifecycle-model.json"
K2=ROOT/"standards/kernel/KERNEL-0002-canonical-object-data-model.md"
K3=ROOT/"standards/kernel/KERNEL-0003-lifecycle-state-machines.md"
A2=ROOT/"reference/kernel/REF-0038-kernel-object-lifecycle-ambiguity-register.md"
ALLOWED={"MUST","MUST NOT","SHOULD","SHOULD NOT","MAY"}

def fm(text):
    end=text.find("\n---\n",4); out={}
    for line in text[4:end].splitlines():
        if line.startswith(" ") or ":" not in line: continue
        k,v=line.split(":",1); out[k.strip()]=v.strip()
    return out

def rows(path,prefix,n):
    out=[]
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| "+prefix):
            c=[x.strip() for x in line.strip().strip("|").split("|")]
            if len(c)!=n: raise ValueError(f"{path}: malformed {prefix} row")
            out.append(c)
    return out

def ids(path,prefix):
    return re.findall(rf"^\|\s*({re.escape(prefix)}\d{{3,4}})\s*\|",path.read_text(encoding="utf-8"),re.M)

def main():
    e=[]
    docs={"KERNEL-0000":"KERNEL-0000-specification-family-index.md",
          "KERNEL-0001":"KERNEL-0001-core-operational-contract.md",
          "KERNEL-0002":"KERNEL-0002-canonical-object-data-model.md",
          "KERNEL-0003":"KERNEL-0003-lifecycle-state-machines.md"}
    for did,name in docs.items():
        p=ROOT/"standards/kernel"/name
        if not p.exists(): e.append("missing "+did); continue
        m=fm(p.read_text(encoding="utf-8"))
        if m.get("id")!=did or m.get("status")!="Draft": e.append(did+" metadata")
    for did in ["KERNEL-0004","KERNEL-0005"]:
        if list((ROOT/"standards/kernel").glob(did+"-*.md")): e.append(did+" exists")

    core=json.loads(CORE.read_text(encoding="utf-8"))
    if core.get("schema")!="mingos.kernel-core-requirements.v0.2": e.append("core schema")
    try: mr=rows(K1,"KCR-",10)
    except ValueError as x: e.append(str(x)); mr=[]
    jr=core.get("requirements",[])
    if len(mr)!=36 or len(jr)!=36: e.append("core requirement count")
    for m,j in zip(mr,jr):
        rid,domain,level,text,scope,treat,sources,methods,evidence,future=m
        level=level.strip("`"); scope=scope.strip("`"); treat=treat.strip("`")
        expected_sources="; ".join(f"{x['source_id']} {x['locator']} [{x['source_role']}]" for x in j.get("source_refs",[]))
        checks=[rid==j.get("id"),domain==j.get("domain"),level==j.get("level"),text==j.get("text"),
                scope==j.get("requirement_scope"),treat==j.get("source_treatment"),
                sources==expected_sources,methods=="; ".join(j.get("verification_methods",[])),
                evidence=="; ".join(j.get("evidence_types",[])),future==j.get("delegated_or_future_detail")]
        if level not in ALLOWED or not all(checks): e.append(rid+" semantic sync")
    commit=core.get("decision_base_commit")
    for sid,x in core.get("source_baseline",{}).items():
        p=ROOT/x["path"]
        if not p.exists(): e.append(sid+" path"); continue
        m=fm(p.read_text(encoding="utf-8"))
        if m.get("id")!=sid or m.get("status")!=x.get("status") or m.get("version")!=x.get("version"): e.append(sid+" metadata")
        try: blob=subprocess.check_output(["git","rev-parse",f"{commit}:{x['path']}"],cwd=ROOT,text=True).strip()
        except subprocess.CalledProcessError: e.append(sid+" unresolved"); continue
        if blob!=x.get("blob_sha"): e.append(sid+" blob")
    if [x[0] for x in rows(A1,"KCA-",8)] != [x["id"] for x in core.get("ambiguities",[])]: e.append("core ambiguities")
    if [x[0] for x in rows(V,"KVT-",4)] != [x["id"] for x in core.get("vocabulary",[])]: e.append("core vocabulary")
    for k,v in {"requirement_count":36,"ambiguity_count":30,"vocabulary_count":30,
                "external_source_count":20,"created_kernel_document_count":4,
                "reserved_not_created_count":2,"implementation_conformance_claim":False}.items():
        if core.get("integrity",{}).get(k)!=v: e.append("core integrity "+k)

    d=json.loads(MODEL.read_text(encoding="utf-8"))
    if d.get("schema")!="mingos.kernel-object-lifecycle-model.v0.1": e.append("model schema")
    if ids(K2,"KOT-") != [x["id"] for x in d["object_types"]]: e.append("object IDs")
    if ids(K2,"KDO-") != [x["id"] for x in d["object_requirements"]]: e.append("object req IDs")
    if ids(K3,"KLS-") != [x["id"] for x in d["lifecycle_requirements"]]: e.append("lifecycle req IDs")
    if ids(A2,"KOLA-") != [x["id"] for x in d["ambiguities"]]: e.append("R8 ambiguity IDs")
    for collection in ("object_requirements","lifecycle_requirements"):
        for x in d[collection]:
            if x["level"] not in ALLOWED: e.append(x["id"]+" level")
    for lc in d["lifecycles"]:
        states=set(lc["states"]); seen=set()
        for a,b in lc["transitions"]:
            if a not in states or b not in states or a==b or (a,b) in seen: e.append(lc["id"]+" transition")
            seen.add((a,b))
    expected={"object_requirement_count":36,"object_type_count":35,"access_class_count":6,
              "lifecycle_requirement_count":34,"lifecycle_count":9,"transition_count":129,
              "ambiguity_count":32,"created_kernel_document_count":4,
              "reserved_not_created_count":2,"implementation_conformance_claim":False}
    for k,v in expected.items():
        if d.get("integrity",{}).get(k)!=v: e.append("model integrity "+k)
    if core.get("review",{}).get("state")!="PreparedNotExecuted" or d.get("review",{}).get("state")!="PreparedNotExecuted": e.append("review")
    if core.get("conformance",{}).get("current_claim")!="NoCurrentKernelConformanceClaim" or d.get("conformance",{}).get("current_claim")!="NoCurrentKernelConformanceClaim": e.append("claim")
    state=(ROOT/"governance/status/GOV-0001-current-canonical-state.md").read_text(encoding="utf-8")
    if "Foundation 1.0 / Day 17" not in state or "1.0.0-alpha.17" not in state: e.append("day17")
    if e:
        print("Round 08 Kernel validation failed:"); [print(" -",x) for x in e]; return 1
    print("Round 08 Kernel validation passed: core semantic/source sync plus 35 objects, 36 object requirements, 9 lifecycles, 129 transitions, 34 lifecycle requirements, 32 ambiguities.")
    return 0
if __name__=="__main__": raise SystemExit(main())
