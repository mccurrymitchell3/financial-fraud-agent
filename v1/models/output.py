from pydantic import BaseModel
from typing import List

class InvestigationReport(BaseModel):
    customer_id: str
    summary: str
    suspicious_patterns: List[str]
    risk_score: int
    escalation_required: bool
    reasoning: str
