def calculate_risk(transactions, sanctions_hits):
    risk = 0
    for tx in transactions:
        if tx["amount"] > 5000:
            risk += 25
        if tx["merchant"] == "Crypto Exchange":
            risk += 20
    risk += len(sanctions_hits) * 30
    return min(risk, 100)
