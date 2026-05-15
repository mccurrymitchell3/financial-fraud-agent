from pydantic import BaseModel
from typing import List, Optional

class InvestigationState(BaseModel):
    customer_id: str
    customer_profile: Optional[dict] = None
    transactions: List[dict] = []
    sanctions_hits: List[str] = []
    policy_findings: List[str] = []
    risk_score: int = 0
    escalation_required: bool = False
    tool_history: List[dict] = []
    reasoning_Steps: List[str] = []
