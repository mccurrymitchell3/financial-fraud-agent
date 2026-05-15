from typing import List

TOOL_DEFINITION = {
    "type": "function",
    "name": "sanctions_check",
    "description": "Check transactions for sanctioned jurisdictions.",
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
            }
        },
        "required": ["transactions"]
    }
}

HIGH_RISK_COUNTRIES = [
    "Cayman Islands",
    "North Korea"
]

def execute(transactions: List) -> List:
    hits = []
    for tx in transactions:
        if tx["country"] in HIGH_RISK_COUNTRIES:
            hits.append(tx["country"])
    return hits
