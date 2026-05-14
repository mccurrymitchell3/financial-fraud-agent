from fastapi import APIRouter
from agents.planner import run_investigation
from agents.investigator import generate_report

router = APIRouter()
@router.get("/investigate/{customer_id}")
def investigate(customer_id: str):
    state = run_investigation(customer_id)
    report = generate_report(state)
    return report
