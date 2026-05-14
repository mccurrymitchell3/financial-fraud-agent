def get_customer_profile(customer_id: str):
    fake_db = {
        "1001": {
            "name": "John Doe",
            "account_age_days": 30,
            "country": "US",
            "kyc_verified": True
        }
    }

    return fake_db.get(customer_id, {})
