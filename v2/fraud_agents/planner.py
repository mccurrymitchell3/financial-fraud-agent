from openai import OpenAI
from dotenv import load_dotenv
from v2.models.output import InvestigationReport
from v2.tools.registry import TOOLS, TOOL_MAP
import json

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = """
You are a financial fraud investigation agent.

Your responsibilities:
- gather evidence
- investigate suspicious activity
- use tools when needed
- NEVER invent data
- use deterministic tools for risk scoring
- escalate when risk is high
"""

def run_agent(customer_id: str):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"Investigate customer {customer_id} for suspicious activity."
        }
    ]

    while True:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=messages,
            tools=TOOLS
        )
        response_output = response.output
        messages.extend(response_output)
        print(response_output)
        tool_calls = []
        for item in response.output:
            if item.type == "function_call":
                tool_calls.append(item)
        # If no tool calls, return
        if not tool_calls:
            final_response = client.responses.parse(
                model="gpt-4.1-mini",
                input=messages + [
                    {
                        "role": "system",
                        "content": (
                            "Generate the final investigation report."
                        )
                    }
                ],
                text_format=InvestigationReport
            )
            return final_response.output_parsed
        # Execute tools
        for tool_call in tool_calls:
            tool_name = tool_call.name
            arguments = json.loads(tool_call.arguments)
            tool_function = TOOL_MAP[tool_name]
            tool_result = tool_function(**arguments)
            messages.append({
                "type": "function_call_output",
                "call_id": tool_call.call_id,
                "output": json.dumps(tool_result)
            })
