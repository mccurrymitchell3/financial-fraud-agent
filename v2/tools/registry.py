from v2.tools.customer_lookup import (
    TOOL_DEFINITION as CUSTOMER_TOOL,
    execute as customer_execute
)
from v2.tools.transactions import (
    TOOL_DEFINITION as TRANSACTION_TOOL,
    execute as transaction_execute
)
from v2.tools.sanctions import (
    TOOL_DEFINITION as SANCTIONS_TOOL,
    execute as sanctions_execute
)
from v2.tools.risk_rules import (
    TOOL_DEFINITION as RISK_TOOL,
    execute as risk_execute
)

TOOLS = [
    CUSTOMER_TOOL,
    TRANSACTION_TOOL,
    SANCTIONS_TOOL,
    RISK_TOOL
]

TOOL_MAP = {
    "get_customer_profile": customer_execute,
    "get_transactions": transaction_execute,
    "sanctions_check": sanctions_execute,
    "calculate_risk": risk_execute
}
