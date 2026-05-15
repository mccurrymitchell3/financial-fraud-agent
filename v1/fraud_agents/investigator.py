from openai import OpenAI
from v1.models.output import InvestigationReport
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
You are a financial fraud investigation assistant.
Rules:
- ONLY use provided evidence
- NEVER speculate
- NEVER invent transactions or risk factors
- If evidence is insufficient, explicitly say so
- Be concise and professional
"""

def generate_report(state):
    investigation_context = f"""
Customer ID:
{state.customer_id}

Customer Profile:
{json.dumps(state.customer_profile, indent=2)}

Transactions:
{json.dumps(state.transactions, indent=2)}

Sanctions Hits:
{json.dumps(state.sanctions_hits, indent=2)}

Policy Findings:
{json.dumps(state.policy_findings, indent=2)}

Deterministic Risk Score:
{state.risk_score}

Escalataion Required:
{state.escalation_required}
"""
    response = client.responses.parse(
        model="gpt-4.1-mini",
        input = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": (
                    "Generate a structured fraud investigation report "
                    "using ONLY the provided evidence.\n\n"
                    f"{investigation_context}"
                )
            }
        ],
        text_format=InvestigationReport
    )
    return response.output_parsed
