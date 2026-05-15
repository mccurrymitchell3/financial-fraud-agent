from typing import Dict

TOOL_DEFINITION = {
    "type": "function",
    "name": "get_customer_profile",
    "description": "Retrieve customer profile information for fraud investigations.",
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

def execute(customer_id: str) -> Dict:
    fake_db = {
        "1001": {
            "name": "John Doe",
            "account_age_days": 30,
            "country": "US",
            "kyc_verified": True
        }
    }

    return fake_db.get(customer_id, {})
