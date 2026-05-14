def retrieve_policy_context(query: str):
    with open("data/policies.txt", "r") as f:
        policies = f.read()
    relevant = []
    for line in policies.splitlines():
        if "Crypto" in query and "Crpyto" in line:
            relevant.append(line)
        if "high-risk" in query and "high-risk" in line:
            relevant.append(line)
    return relevant
