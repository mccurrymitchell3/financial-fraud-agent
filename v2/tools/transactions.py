from typing import List

TOOL_DEFINITION = {
    "type": "function",
    "name": "get_transactions",
    "description": "Retrieve recent customer transactions.",
    "parameters": {
        "type": "object",
        "properties": {
            "customer_id": {
                "type": "string"
            }
        },
        "required": ["customer_id"]
    }
}

def execute(customer_id: str) -> List:
    return [
        {
            "amount": 8000,
            "merchant": "Crypto Exchange",
            "country": "Cayman Islands"
        },
        {
            "amount": 120,
            "merchant": "Amazon",
            "country": "US"
        }
    ]
