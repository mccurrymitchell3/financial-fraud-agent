from fastapi import APIRouter
from v1.fraud_agents.planner import run_investigation as run_v1_investigation
from v1.fraud_agents.investigator import generate_report as generate_v1_report
from v2.fraud_agents.planner import run_agent

router = APIRouter()


@router.get("/investigate/{customer_id}")
@router.get("/v1/investigate/{customer_id}")
def investigate_v1(customer_id: str):
    state = run_v1_investigation(customer_id)
    report = generate_v1_report(state)
    return report


@router.get("/v2/investigate/{customer_id}")
def investigate_v2(customer_id: str):
    result = run_agent(customer_id)
    return {"result": result}
