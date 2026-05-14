from models.state import InvestigationState
from tools.customer_lookup import get_customer_profile
from tools.transactions import get_transactions
from tools.sanctions import sanctions_check
from tools.risk_rules import calculate_risk
from tools.policy_rag import retrieve_policy_context

def run_investigation(customer_id: str):
    state = InvestigationState(customer_id=customer_id)
    state.customer_profile = get_customer_profile(customer_id=customer_id)
    state.transactions = get_transactions(customer_id=customer_id)
    state.sanctions_hits = sanctions_check(transactions=state.transactions)
    state.policy_findings = retrieve_policy_context(query="Crypto high-risk")
    state.risk_score = calculate_risk(
        state.transactions,
        state.sanctions_hits
    )
    if state.risk_score >= 70:
        state.escalation_required = True
    return state
