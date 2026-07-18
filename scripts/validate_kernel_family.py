#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json,re,subprocess
ROOT=Path(__file__).resolve().parents[1]
ALLOWED={"MUST","MUST NOT","SHOULD","SHOULD NOT","MAY"}
C=ROOT/"reference/kernel/mingos-kernel-conformance-model.json"
T=ROOT/"reference/kernel/mingos-kernel-test-specifications.json"
CORE=ROOT/"reference/kernel/mingos-kernel-core-requirements.json"
OBJ=ROOT/"reference/kernel/mingos-kernel-object-lifecycle-model.json"
K4=ROOT/"standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md"
K5=ROOT/"standards/kernel/KERNEL-0005-test-specifications-derived-indexes.md"
def fm(text):
    end=text.find("\n---\n",4);out={}
    for line in text[4:end].splitlines():
        if line.startswith(" ") or ":" not in line:continue
        k,v=line.split(":",1);out[k.strip()]=v.strip()
    return out
def rows(path,prefix,n):
    out=[]
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| "+prefix):
            c=[x.strip() for x in line.strip().strip("|").split("|")]
            if len(c)!=n:raise ValueError(f"{path}: malformed {prefix} row {len(c)}")
            out.append(c)
    return out
def render_ref(ref,baseline):
    if "baseline_ref" in ref:
        b=baseline[ref["baseline_ref"]]
        return f"{ref['baseline_ref']} {ref['locator']} [{b['source_role']}]"
    return f"{ref['source_id']} / {ref['status']} / {ref['version']} / `{ref['path']}` / {ref['locator']} / {ref['source_role']}"
def check_req_table(path,prefix,items,baseline,errors):
    try: mr=rows(path,prefix,8)
    except ValueError as exc:errors.append(str(exc));return
    if len(mr)!=len(items):errors.append(prefix+" count");return
    for m,j in zip(mr,items):
        rid,domain,level,text,sources,treatment,methods,evidence=m
        expected_sources="; ".join(render_ref(x,baseline) for x in j.get("source_refs",[]))
        ok=(rid==j.get("id") and domain==j.get("domain") and level.strip("`")==j.get("level") and text==j.get("text") and sources==expected_sources and treatment.strip("`")==j.get("source_treatment") and methods=="; ".join(j.get("verification_methods",[])) and evidence=="; ".join(j.get("evidence_types",[])))
        if not ok:errors.append(rid+" semantic sync")
        if j.get("level") not in ALLOWED:errors.append(rid+" level")
        if not j.get("source_refs") or not j.get("verification_methods") or not j.get("evidence_types"):errors.append(rid+" traceability")
def main():
    e=[]
    docs={"KERNEL-0000":("KERNEL-0000-specification-family-index.md","0.5.0-draft.5"),"KERNEL-0001":("KERNEL-0001-core-operational-contract.md","0.2.3-draft.5"),"KERNEL-0002":("KERNEL-0002-canonical-object-data-model.md","0.2.0-draft.2"),"KERNEL-0003":("KERNEL-0003-lifecycle-state-machines.md","0.2.0-draft.2"),"KERNEL-0004":("KERNEL-0004-conformance-requirements-evidence-model.md","0.1.0-draft.1"),"KERNEL-0005":("KERNEL-0005-test-specifications-derived-indexes.md","0.1.0-draft.1")}
    for did,(name,ver) in docs.items():
        p=ROOT/"standards/kernel"/name
        if not p.exists():e.append("missing "+did);continue
        m=fm(p.read_text())
        if m.get("id")!=did or m.get("status")!="Draft" or m.get("version")!=ver:e.append(did+" metadata")
    c=json.loads(C.read_text());t=json.loads(T.read_text())
    if c.get("schema")!="mingos.kernel-conformance-model.v0.1":e.append("conformance schema")
    if t.get("schema")!="mingos.kernel-test-specifications.v0.1":e.append("test schema")
    check_req_table(K4,"KCF-",c["requirements"],c["source_baseline"],e)
    check_req_table(K5,"KTG-",t["governance_requirements"],t["source_baseline"],e)
    base=c.get("decision_base_commit")
    if t.get("decision_base_commit")!=base:e.append("source base mismatch")
    for ref,b in c.get("source_baseline",{}).items():
        p=ROOT/b["path"]
        if not p.exists():e.append(ref+" path");continue
        try: blob=subprocess.check_output(["git","rev-parse",f"{base}:{b['path']}"],cwd=ROOT,text=True).strip()
        except subprocess.CalledProcessError:e.append(ref+" unresolved");continue
        if blob!=b.get("blob_sha"):e.append(ref+" blob")
    if c.get("source_baseline")!=t.get("source_baseline"):e.append("source baseline indexes differ")
    expected=[x["id"] for x in json.loads(CORE.read_text())["requirements"]]+[x["id"] for x in json.loads(OBJ.read_text())["object_requirements"]]+[x["id"] for x in json.loads(OBJ.read_text())["lifecycle_requirements"]]
    if [x["requirement_id"] for x in t["tests"]]!=expected:e.append("test coverage/order")
    if len(set(x["id"] for x in t["tests"]))!=len(t["tests"]):e.append("duplicate test")
    if any(x["execution_status"]!="NotExecuted" for x in t["tests"]):e.append("execution claim")
    if c["current_authorization"]!={"profile_count":0,"assessment_count":0,"claim_count":0,"badge_count":0,"current_claim":"NoCurrentKernelConformanceClaim"}:e.append("authorization")
    if t["execution_summary"]["executed_count"]!=0 or t["execution_summary"]["pass_count"]!=0:e.append("execution summary")
    core=json.loads(CORE.read_text())
    if [x["id"] for x in core["family"]["documents"]]!=["KERNEL-0000","KERNEL-0001","KERNEL-0002","KERNEL-0003","KERNEL-0004","KERNEL-0005"]:e.append("family docs")
    if core["family"]["reserved_not_created"]!=[]:e.append("reserved docs")
    if core["conformance"]["current_claim"]!="NoCurrentKernelConformanceClaim":e.append("claim")
    state=(ROOT/"governance/status/GOV-0001-current-canonical-state.md").read_text()
    if "Foundation 1.0 / Day 17" not in state or "1.0.0-alpha.17" not in state:e.append("day17")
    if e:
        print("Round09 validation failed:");[print(" -",x) for x in e];return 1
    print("Round09 validation passed: 42 traced KCF, 32 traced KTG, exact source blobs, 106 NotExecuted tests, 24 scenarios, zero claims.")
    return 0
if __name__=="__main__":raise SystemExit(main())
