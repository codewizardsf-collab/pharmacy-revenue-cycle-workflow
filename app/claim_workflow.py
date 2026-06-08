def classify_denial(reason_code: str) -> str:
    mapping = {
        "PA_REQUIRED": "prior_authorization",
        "INVALID_NDC": "coding_error",
        "COVERAGE_EXPIRED": "eligibility",
    }
    return mapping.get(reason_code, "manual_review")


def next_action(status: str, denial_reason: str | None = None) -> str:
    if status == "paid":
        return "close_claim"
    if status == "denied":
        return f"route_to_{classify_denial(denial_reason or '')}_queue"
    return "monitor_status"
