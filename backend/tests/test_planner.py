from graph.planner import needs_planning

def test_simple_calculation_skips_planning():
    state = {"messages": [{"role": "user", "content": "What is 15% of 840?"}]}
    assert needs_planning(state) is False

def test_complex_request_needs_planning():
    state = {"messages": [{"role": "user", "content": "Summarise my notes and create tasks for the hard topics"}]}
    assert needs_planning(state) is True