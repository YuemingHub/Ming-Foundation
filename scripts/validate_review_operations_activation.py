#!/usr/bin/env python3
"""Validate Day 16 review operations controls without fabricating activation."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def load(rel): return json.loads((ROOT/rel).read_text(encoding="utf-8"))
def main():
 errors=[]
 roles=load("standards/review/REVIEW_ROLE_ASSIGNMENT_REGISTRY.json")
 if len(roles["roles"])!=8 or roles["summary"]!={"roles_defined":8,"roles_assigned":0,"conflict_checks_complete":0,"qualification_checks_complete":0}: errors.append("role registry summary mismatch")
 for r in roles["roles"]:
  if r["assignment_state"]!="Unassigned" or r["assignee"] is not None or r["may_authorize_human_review"] is not False: errors.append(f"{r['role_id']}: fabricated assignment or authority")
 protocols=load("standards/review/REVIEW_PROTOCOL_APPROVAL_REGISTRY.json")
 if len(protocols["protocols"])!=7 or protocols["summary"]!={"protocols_defined":7,"synthetic_use_approved":7,"human_use_approved":0,"human_use_blocked":7}: errors.append("protocol summary mismatch")
 for p in protocols["protocols"]:
  if p["synthetic_use_authorized"] is not True or p["human_use_state"]!="NotApproved" or p["human_approver"] is not None: errors.append(f"{p['approval_id']}: human approval boundary mismatch")
 env=load("standards/review/RESTRICTED_EVIDENCE_ENVIRONMENT.json")
 if len(env["controls"])!=8 or env["design_state"]!="Complete" or env["live_environment_state"]!="NotProvisioned": errors.append("environment state mismatch")
 if env["live_evidence_ingestion"]!="Prohibited" or env["synthetic_data_only"] is not True: errors.append("evidence ingestion boundary mismatch")
 if any(c["live_state"] in {"Ready","Configured","Provisioned"} for c in env["controls"]): errors.append("live control fabricated as ready")
 activation=load("standards/review/REVIEW_OPERATIONAL_ACTIVATION.json")
 if activation["summary"]["roles_assigned"]!=0 or activation["summary"]["approvals_completed"]!=0 or activation["summary"]["environment_controls_ready"]!=0: errors.append("activation readiness counts must remain zero")
 if errors:
  print("Review-operations activation validation failed:")
  for e in errors: print(" -",e)
  return 1
 print("Review-operations activation validation passed. Validated 8 unassigned roles, zero conflict and qualification completions, 7 synthetic-use protocol designs with zero human-use approvals, 8 completed environment designs with zero live controls ready, and prohibited live evidence ingestion.")
 return 0
if __name__=="__main__": raise SystemExit(main())
