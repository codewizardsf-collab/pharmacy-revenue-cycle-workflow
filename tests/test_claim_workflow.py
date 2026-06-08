from app.claim_workflow import next_action


def test_prior_authorization_denial_routes_to_pa_queue():
    assert next_action("denied", "PA_REQUIRED") == "route_to_prior_authorization_queue"
