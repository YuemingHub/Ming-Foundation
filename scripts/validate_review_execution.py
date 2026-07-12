#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
def status(p):
    t=(ROOT/p).read_text(encoding="utf-8"); end=t.find("\n---\n",4)
    for line in t[4:end].splitlines():
        if line.startswith("status:"): return line.split(":",1)[1].strip()
def main():
    e=[]
    r=load("standards/review/RFC_INTERNAL_REVIEW_RESULTS.json")
    scope=r["review_scope"]
    if scope["round"]!="InternalArchitectureRound1" or scope["complete"] is not True:e.append("internal review scope")
    for k in ["external_review_complete","affected_person_review_complete","legal_review_complete","implementation_conformance_complete"]:
        if scope[k] is not False:e.append(k)
    results=r["results"]; rfcs={x["source_document"] for x in results}
    if rfcs!={f"RFC-{i:04d}" for i in range(1,6)}:e.append("RFC coverage")
    c={"Pass":0,"Revise":0,"Blocked":0}
    rev=set(); dis=set(); amb=set()
    expected={"scope_and_definitions","architecture_and_data_model","human_agency_and_ethics","privacy_and_consent",
    "safety_and_escalation","implementation_and_conformance","affected_person_or_domain_review","compatibility_and_migration","evidence_and_limitations"}
    for x in results:
        if x["review_state"]!="Complete" or x["promotion_recommendation"]!="RetainProposed":e.append(x["source_document"])
        if {d["dimension"] for d in x["dimensions"]}!=expected:e.append("dimensions")
        for d in x["dimensions"]: c[d["disposition"]]+=1
        rev.update(x["revision_item_refs"]); dis.update(x["dissent_refs"]); amb.update(x["ambiguity_refs"])
    if c!={"Pass":6,"Revise":29,"Blocked":10}:e.append(f"counts {c}")
    p=load("standards/review/RFC_REVISION_PLAN.json"); ids={x["revision_id"] for x in p["items"]}
    if len(ids)!=23 or p["target_status_after_revision"]!="Proposed" or not rev.issubset(ids):e.append("revision plan")
    a=load("standards/review/RFC_AMBIGUITIES.json")["ambiguities"]
    aids={x["ambiguity_id"] for x in a}
    if len(aids)!=19 or any(x["status"]!="Open" or x["review_disposition"]!="RequiresRFCRevision" for x in a):e.append("ambiguities")
    if not amb.issubset(aids):e.append("ambiguity refs")
    d=load("standards/review/RFC_DISSENT_REGISTER.json")["items"]; dids={x["dissent_id"] for x in d}
    if len(dids)!=8 or any(x["status"]!="Open" for x in d) or not dis.issubset(dids):e.append("dissent")
    q=load("standards/requirements/RFC_REQUIREMENTS.json")["requirements"]
    if len(q)!=63 or any(not x.get("internal_review_ref") for x in q):e.append("requirements")
    b=load("standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json")
    if b["results"]!=[] or b["internal_review_execution"]["results_populated"] is not False:e.append("baseline")
    paths=[
    "standards/rfc/RFC-0001-subject-speaker-and-contestability.md",
    "standards/rfc/RFC-0002-consent-and-data-rights-lifecycle.md",
    "standards/rfc/RFC-0003-safety-escalation-handoff-appeal-and-incident.md",
    "standards/rfc/RFC-0004-case-and-cross-family-evidence-governance.md",
    "standards/rfc/RFC-0005-public-claim-charter-sync-and-capability-status.md"]
    if any(status(p)!="Proposed" for p in paths):e.append("RFC status")
    if e:
        print("Review-execution validation failed:")
        for x in e:print(" -",x)
        return 1
    print("Review-execution validation passed. Validated 5 reviews, 45 dimensions, 23 revision items, 19 open ambiguities, 8 open dissent items, and an empty implementation baseline.")
    return 0
if __name__=="__main__": raise SystemExit(main())
