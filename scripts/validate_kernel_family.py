#!/usr/bin/env python3
"""Validate Round 07 Kernel family, exact source baseline, and semantic sync."""
from pathlib import Path
import json, re, subprocess

ROOT=Path(__file__).resolve().parents[1]
K0=ROOT/"standards/kernel/KERNEL-0000-specification-family-index.md"
K1=ROOT/"standards/kernel/KERNEL-0001-core-operational-contract.md"
A=ROOT/"reference/kernel/REF-0032-kernel-core-ambiguity-register.md"
V=ROOT/"reference/kernel/REF-0034-kernel-core-vocabulary-status-map.md"
J=ROOT/"reference/kernel/mingos-kernel-core-requirements.json"
ALLOWED={"MUST","MUST NOT","SHOULD","SHOULD NOT","MAY"}
REQUIRED=["purpose","scope and non-goals","definitions","normative","data and process model",
          "human agency","privacy","safety","review","examples","limitations","version and change history"]

def fm(text):
    end=text.find("\n---\n",4)
    out={}
    for line in text[4:end].splitlines():
        if line.startswith(" ") or ":" not in line: continue
        k,v=line.split(":",1); out[k.strip()]=v.strip()
    return out

def rows(path,prefix,n):
    result=[]
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| "+prefix):
            cells=[x.strip() for x in line.strip().strip("|").split("|")]
            if len(cells)!=n: raise ValueError(f"{path}: expected {n} cells, got {len(cells)}")
            result.append(cells)
    return result

def main():
    errors=[]
    for did,path in {"KERNEL-0000":K0,"KERNEL-0001":K1}.items():
        m=fm(path.read_text(encoding="utf-8"))
        if m.get("id")!=did or m.get("status")!="Draft": errors.append(f"{did} metadata")
        low=path.read_text(encoding="utf-8").lower()
        for section in REQUIRED:
            if section not in low: errors.append(f"{did} missing MOS content: {section}")
    for did in ["KERNEL-0002","KERNEL-0003","KERNEL-0004","KERNEL-0005"]:
        if list((ROOT/"standards/kernel").glob(did+"-*.md")): errors.append(f"{did} unexpectedly exists")
    data=json.loads(J.read_text(encoding="utf-8"))
    if data.get("schema")!="mingos.kernel-core-requirements.v0.2": errors.append("schema")
    try: mr=rows(K1,"KCR-",10)
    except ValueError as e: errors.append(str(e)); mr=[]
    jr=data.get("requirements",[])
    if len(mr)!=36 or len(jr)!=36: errors.append("requirement count")
    for m,j in zip(mr,jr):
        rid,domain,level,text,scope,treat,sources,methods,evidence,future=m
        level=level.strip("`"); scope=scope.strip("`"); treat=treat.strip("`")
        if level not in ALLOWED: errors.append(f"{rid} level")
        expected_sources="; ".join(f"{x['source_id']} {x['locator']} [{x['source_role']}]" for x in j.get("source_refs",[]))
        pairs=[("id",rid,j.get("id")),("domain",domain,j.get("domain")),("level",level,j.get("level")),
               ("text",text,j.get("text")),("scope",scope,j.get("requirement_scope")),
               ("treatment",treat,j.get("source_treatment")),("sources",sources,expected_sources),
               ("methods",methods,"; ".join(j.get("verification_methods",[]))),
               ("evidence",evidence,"; ".join(j.get("evidence_types",[]))),
               ("future",future,j.get("delegated_or_future_detail"))]
        for name,a,b in pairs:
            if a!=b: errors.append(f"{rid} {name} mismatch")
        if not j.get("source_refs") or not j.get("verification_methods") or not j.get("evidence_types"):
            errors.append(f"{rid} incomplete")
    commit=data.get("decision_base_commit")
    for sid,e in data.get("source_baseline",{}).items():
        p=ROOT/e["path"]
        if not p.exists(): errors.append(f"{sid} path"); continue
        m=fm(p.read_text(encoding="utf-8"))
        if m.get("id")!=sid or m.get("status")!=e.get("status") or m.get("version")!=e.get("version"):
            errors.append(f"{sid} metadata baseline")
        try: blob=subprocess.check_output(["git","rev-parse",f"{commit}:{e['path']}"],cwd=ROOT,text=True).strip()
        except subprocess.CalledProcessError: errors.append(f"{sid} unresolved"); continue
        if blob!=e.get("blob_sha"): errors.append(f"{sid} blob")
    if [x[0] for x in rows(A,"KCA-",8)] != [x["id"] for x in data.get("ambiguities",[])]: errors.append("ambiguities")
    if [x[0] for x in rows(V,"KVT-",4)] != [x["id"] for x in data.get("vocabulary",[])]: errors.append("vocabulary")
    integ=data.get("integrity",{})
    for k,v in {"requirement_count":36,"ambiguity_count":30,"vocabulary_count":30,
                "external_source_count":20,"created_kernel_document_count":2,
                "reserved_not_created_count":4,"implementation_conformance_claim":False}.items():
        if integ.get(k)!=v: errors.append("integrity "+k)
    if data.get("review",{}).get("state")!="PreparedNotExecuted": errors.append("review")
    if data.get("conformance",{}).get("current_claim")!="NoCurrentKernelConformanceClaim": errors.append("claim")
    state=(ROOT/"governance/status/GOV-0001-current-canonical-state.md").read_text(encoding="utf-8")
    if "Foundation 1.0 / Day 17" not in state or "1.0.0-alpha.17" not in state: errors.append("day17")
    if errors:
        print("Kernel validation failed:"); [print(" -",x) for x in errors]; return 1
    print("Kernel validation passed: 36 semantically synchronized requirements, 20-source exact baseline, 30 ambiguities, 30 vocabulary items.")
    return 0
if __name__=="__main__": raise SystemExit(main())
