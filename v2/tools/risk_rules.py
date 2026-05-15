from typing import List

TOOL_DEFINITION = {
    "type": "function",
    "name": "calculate_risk",
    "description": "Calculate deterministic fraud risk score.",
    "parameters": {
        "type": "object",
        "properties": {
            "transactions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "amount": {"type": "number"},
                        "merchant": {"type": "string"},
                        "country": {"type": "string"}
                    },
                    "required": ["amount", "merchant", "country"],
                    "additionalProperties": False
                }
            },
            "sanctions_hits": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            }
        },
        "required": ["transactions", "sanctions_hits"]
    }
}

def execute(transactions: List, sanctions_hits: List) -> int:
    risk = 0
    for tx in transactions:
        if tx["amount"] > 5000:
            risk += 25
        if tx["merchant"] == "Crypto Exchange":
            risk += 20
    risk += len(sanctions_hits) * 30
    return min(risk, 100)
