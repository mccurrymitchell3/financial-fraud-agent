from pydantic import BaseModel, Field
from typing import List

class InvestigationReport(BaseModel):
    customer_id: str = Field(
        description="Customer under investigation"
    )
    summary: str = Field(
        description="High-level investigation summary"
    )
    suspicious_patterns: List[str] = Field(
        description="Detected suspicious behaviors"
    )
    risk_score: int = Field(
        description="Deterministic risk score",
        ge=0,
        le=100
    )
    escalation_required: bool = Field(
        description="Whether human escalation is required"
    )
    reasoning: str = Field(
        description="Detailed evidence-based reasoning"
    )
