#!/usr/bin/env python3
"""Validate Day 16 controlled-pilot classification and synthetic results."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def load(rel): return json.loads((ROOT/rel).read_text(encoding="utf-8"))
def main():
 errors=[]
 auth=load("standards/review/CONTROLLED_PILOT_AUTHORIZATION.json")
 if auth["overall_state"]!="SyntheticOnlyAuthorized" or auth["authorized_classes"]!=["CP0","CP1"] or auth["blocked_classes"]!=["CP2","CP3"]: errors.append("pilot authorization mismatch")
 states={c["class_id"]:(c["authorization_state"],c["execution_state"]) for c in auth["classes"]}
 if states!={"CP0":("Authorized","Complete"),"CP1":("Authorized","Complete"),"CP2":("Blocked","NotExecuted"),"CP3":("Blocked","NotExecuted")}: errors.append("pilot class state mismatch")
 for k in ["human_review_authorized","recruitment_authorized","participant_sessions_authorized","live_evidence_authorized","product_decision_effect_authorized","public_conformance_claim_authorized"]:
  if auth[k] is not False: errors.append(f"{k} must remain false")
 scenarios=load("standards/review/SYNTHETIC_PILOT_SCENARIOS.json")
 results=load("standards/review/SYNTHETIC_PILOT_RESULTS.json")
 if len(scenarios["scenarios"])!=12 or len(results["results"])!=12: errors.append("scenario count mismatch")
 if scenarios["data_policy"]!="SyntheticOnly" or results["data_policy"]!="SyntheticOnly": errors.append("data policy mismatch")
 scenario_ids={x["scenario_id"] for x in scenarios["scenarios"]}
 if scenario_ids!={x["scenario_id"] for x in results["results"]}: errors.append("scenario/result coverage mismatch")
 for s in scenarios["scenarios"]:
  if s["contains_real_person_data"] is not False or s["contains_sensitive_case_data"] is not False or s["input_class"]!="SyntheticFixture": errors.append(f"{s['scenario_id']}: non-synthetic fixture")
 for r in results["results"]:
  if r["result"]!="Pass" or r["synthetic_only"] is not True or r["real_evidence_detected"] is not False: errors.append(f"{r['scenario_id']}: result boundary mismatch")
 expected={"executed":12,"passed":12,"failed":0,"stopped":0,"real_evidence_detected":0}
 if results["summary"]!=expected: errors.append("result summary mismatch")
 for k in ["participants_recruited","participant_sessions","participant_evidence_records","live_system_actions","implementation_conformance_results"]:
  if results[k]!=0: errors.append(f"{k} must remain zero")
 gate=load("standards/review/DAY16_OPERATIONAL_READINESS_GATE.json")
 if gate["overall_state"]!="SyntheticPilotAuthorizedHumanPilotBlocked" or gate["summary"]!={"gate_items":14,"pass":9,"blocked":5,"fail":0}: errors.append("Day16 gate mismatch")
 baseline=load("standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json")
 if baseline["results"]!=[] or baseline["day16_controlled_pilot"]["implementation_tests_executed"]!=0: errors.append("implementation conformance boundary mismatch")
 if errors:
  print("Controlled-pilot validation failed:")
  for e in errors: print(" -",e)
  return 1
 print("Controlled-pilot validation passed. Validated CP0 and CP1 authorization and completion, CP2 and CP3 blocking, 12 passed synthetic scenarios, zero real evidence, zero participants, zero live actions, zero implementation tests, a 14-item Day16 gate (9 Pass, 5 Blocked), and an empty implementation-conformance baseline.")
 return 0
if __name__=="__main__": raise SystemExit(main())
