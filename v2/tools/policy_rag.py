from pathlib import Path


def retrieve_policy_context(query: str):
    policy_path = Path(__file__).resolve().parents[1] / "data" / "policies.txt"
    with policy_path.open("r") as f:
        policies = f.read()
    relevant = []
    for line in policies.splitlines():
        if "Crypto" in query and "Crpyto" in line:
            relevant.append(line)
        if "high-risk" in query and "high-risk" in line:
            relevant.append(line)
    return relevant
