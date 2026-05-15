HIGH_RISK_COUNTRIES = [
    "Cayman Islands",
    "North Korea"
]

def sanctions_check(transactions):
    hits = []
    for tx in transactions:
        if tx["country"] in HIGH_RISK_COUNTRIES:
            hits.append(tx["country"])
    return hits
