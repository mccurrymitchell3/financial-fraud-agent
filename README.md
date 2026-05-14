# Financial Fraud Agent

Financial Fraud Agent is a small FastAPI application that demonstrates a fraud investigation workflow. It combines deterministic checks, policy lookup, and an OpenAI-powered report generator to produce a structured investigation report for a customer.

The project is intentionally simple: the customer data, transactions, sanctions list, and policy retrieval are local mock implementations. That makes the application useful as a learning scaffold for how a fraud workflow can be decomposed into tools, state, orchestration, and final reporting.

## What It Does

The application exposes one investigation endpoint:

```http
GET /investigate/{customer_id}
```

When called, the app:

1. Creates an `InvestigationState` for the requested customer.
2. Looks up the customer profile.
3. Retrieves recent transactions.
4. Checks transactions against high-risk jurisdictions.
5. Retrieves relevant policy text from `data/policies.txt`.
6. Calculates a deterministic risk score.
7. Marks the case for escalation when the risk score is at least `70`.
8. Sends the collected evidence to OpenAI to generate a structured fraud investigation report.

## Project Structure

```text
.
├── app.py
├── api/
│   └── routes.py
├── agents/
│   ├── planner.py
│   └── investigator.py
├── models/
│   ├── state.py
│   └── output.py
├── tools/
│   ├── customer_lookup.py
│   ├── transactions.py
│   ├── sanctions.py
│   ├── risk_rules.py
│   └── policy_rag.py
├── data/
│   └── policies.txt
└── requirements.txt
```

## Inner Workings

### API Layer

`app.py` creates the FastAPI application and registers the router from `api/routes.py`.

`api/routes.py` defines the `/investigate/{customer_id}` endpoint. The route is intentionally thin: it calls the investigation planner, passes the resulting state to the investigator, and returns the final report.

### Investigation State

`models/state.py` defines `InvestigationState`, the shared object passed through the workflow. It stores:

- `customer_id`
- `customer_profile`
- `transactions`
- `sanctions_hits`
- `policy_findings`
- `risk_score`
- `escalation_required`

This state object acts as the case file for the investigation.

### Planner

`agents/planner.py` orchestrates the deterministic part of the investigation. It does not call the language model. Instead, it coordinates local tools and builds the evidence bundle:

- `get_customer_profile()` returns mock customer details.
- `get_transactions()` returns mock transaction data.
- `sanctions_check()` flags transactions involving configured high-risk countries.
- `retrieve_policy_context()` reads relevant policy lines from `data/policies.txt`.
- `calculate_risk()` computes a rule-based risk score.

The planner sets `escalation_required` to `True` when the risk score is `70` or higher.

### Risk Rules

`tools/risk_rules.py` contains simple deterministic scoring logic:

- Transactions over `5000` add `25` risk points.
- Transactions at `"Crypto Exchange"` add `20` risk points.
- Each sanctions/high-risk country hit adds `30` risk points.
- The final score is capped at `100`.

These rules make the risk score auditable before the model generates any narrative.

### Report Generation

`agents/investigator.py` turns the completed investigation state into a structured report using OpenAI.

The investigator:

1. Loads environment variables with `dotenv`.
2. Creates an OpenAI client.
3. Builds a text evidence packet from the investigation state.
4. Sends the packet to the Responses API.
5. Parses the response into the `InvestigationReport` Pydantic model from `models/output.py`.

The system prompt instructs the model to use only the provided evidence, avoid speculation, and be concise.

### Output Model

`models/output.py` defines the final report schema:

- `customer_id`
- `summary`
- `suspicious_patterns`
- `risk_score`
- `escalation_required`
- `reasoning`

Because the response is parsed into this Pydantic model, the API returns a predictable structured payload instead of free-form text.

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file with your OpenAI API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Running the App

Start the FastAPI development server:

```bash
uvicorn app:app --reload
```

Then call the investigation endpoint:

```bash
curl http://127.0.0.1:8000/investigate/1001
```

## Current Limitations

- Customer and transaction data are mocked in local Python files.
- The sanctions check is a simple high-risk country list, not a real sanctions screening service.
- Policy retrieval is a basic text-file scan, not a true vector search or retrieval system.
- The risk score is deterministic but intentionally minimal.
- The project is a prototype and should not be used for real financial investigations without production data sources, validation, logging, audit controls, and compliance review.

