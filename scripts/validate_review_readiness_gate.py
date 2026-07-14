#!/usr/bin/env python3
"""Validate Profile Round 2 and the current affected-person review gate."""
from pathlib import Path
import json
from validation_utils import canonical_text_blob_sha
ROOT=Path(__file__).resolve().parents[1]
PROFILE_PATHS={
"PROF-0001":ROOT/"standards/profiles/PROF-0001-participation-and-representative-decision-profile.md",
"PROF-0002":ROOT/"standards/profiles/PROF-0002-representative-authority-evidence-profile.md",
"PROF-0003":ROOT/"standards/profiles/PROF-0003-retention-and-backup-completion-profile.md",
"PROF-0004":ROOT/"standards/profiles/PROF-0004-service-response-and-resource-freshness-profile.md"}
def load(rel): return json.loads((ROOT/rel).read_text(encoding="utf-8"))
def main():
 errors=[]
 review=load("standards/review/PROFILE_INTERNAL_REVIEW_ROUND2_RESULTS.json")
 s=review["summary"]
 if (s["profile_count"],s["dimension_count"],s["pass"],s["revise"],s["blocked"])!=(4,32,28,0,4): errors.append("Profile Round 2 summary mismatch")
 for item in review["results"]:
  pid=item["source_document"]
  if item["source_blob_sha"]!=canonical_text_blob_sha(PROFILE_PATHS[pid]): errors.append(f"{pid}: source blob mismatch")
  if item["overall_disposition"]!="InternallyReadyPendingAffectedPersonReview": errors.append(f"{pid}: disposition mismatch")
 gate=load("standards/review/AFFECTED_PERSON_REVIEW_READINESS_GATE.json")
 if gate["overall_state"]!="SyntheticPilotAuthorizedHumanPilotBlocked": errors.append("gate state mismatch")
 if gate["summary"]!={"gate_items":14,"pass":10,"blocked":4,"fail":0}: errors.append("gate counts mismatch")
 if gate.get("synthetic_pilot_authorized") is not True or gate.get("synthetic_pilot_execution_state")!="Complete": errors.append("synthetic pilot state mismatch")
 for key in ["human_pilot_authorized","operationally_ready_to_schedule","recruitment_authorized","sessions_authorized","participant_evidence_exists"]:
  if gate.get(key) is not False: errors.append(f"{key} must remain false")
 activation=load("standards/review/REVIEW_OPERATIONAL_ACTIVATION.json")
 if activation["activation_state"]!="SyntheticPilotOnly" or activation["human_review_activation_state"]!="NotActivated": errors.append("activation state mismatch")
 if len(activation["roles"])!=8 or any(r["assignment_state"]!="Unassigned" or r["assignee"] is not None for r in activation["roles"]): errors.append("roles must remain unassigned")
 if len(activation["approvals"])!=7 or any(a["state"]!="NotApproved" or a["human_use_state"]!="NotApproved" for a in activation["approvals"]): errors.append("human approvals must remain NotApproved")
 for k in ["scheduling_authorized","recruitment_authorized","sessions_authorized"]:
  if activation[k] is not False: errors.append(f"activation {k} must remain false")
 plan=load("standards/review/AFFECTED_PERSON_REVIEW_PLAN.json")
 if plan["execution_state"]!="PreparedNotExecuted": errors.append("human review execution state mismatch")
 for k in ["participants_recruited","sessions_completed","results_recorded"]:
  if plan["summary"][k]!=0: errors.append(f"{k} must remain zero")
 residual=load("standards/review/RFC_R2_RESIDUAL_PLAN.json")
 states={x["item_id"]:x["status"] for x in residual["items"]}
 if states.get("R2R-007")!="SyntheticPilotAuthorizedHumanPilotBlocked": errors.append("R2R-007 state mismatch")
 profiles=load("standards/profiles/RESIDUAL_PROFILE_REGISTRY.json")
 if any(x["status"]!="Proposed" or x["operational_readiness"]!="Blocked" for x in profiles["profiles"]): errors.append("Profile status boundary mismatch")
 amb=load("standards/review/RFC_AMBIGUITIES.json")
 if len(amb["ambiguities"])!=19 or any(x["status"]!="Open" for x in amb["ambiguities"]): errors.append("ambiguity boundary mismatch")
 dissent=load("standards/review/RFC_DISSENT_REGISTER.json")
 if len(dissent["items"])!=8 or any(x["status"]!="Open" for x in dissent["items"]): errors.append("dissent boundary mismatch")
 tests=load("standards/requirements/RFC_ACCEPTANCE_TESTS.json")
 if len(tests["tests"])!=115 or any(x["test_state"]!="SpecificationOnly" for x in tests["tests"]): errors.append("implementation tests must remain specifications")
 baseline=load("standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json")
 if baseline["results"]!=[]: errors.append("implementation baseline must remain empty")
 if errors:
  print("Review-readiness gate validation failed:")
  for e in errors: print(" -",e)
  return 1
 print("Review-readiness gate validation passed. Validated 4 Profile Round 2 reviews, a 14-item affected-person gate (10 Pass, 4 Blocked), synthetic-only activation, 8 unassigned roles, 7 human-use protocols not approved, zero participants and sessions, 19 open ambiguities, 8 open dissent items, 115 unexecuted implementation test specifications, and an empty implementation baseline.")
 return 0
if __name__=="__main__": raise SystemExit(main())
