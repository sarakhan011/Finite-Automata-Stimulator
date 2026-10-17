def example_nfa_contains_01():
    """NFA over {0,1} accepting strings that contain the substring '01'."""
    return NFA(
        states={"q0", "q1", "q2"},
        alphabet={"0", "1"},
        transitions={
            ("q0", "0"): {"q0", "q1"},
            ("q0", "1"): {"q0"},
            ("q1", "1"): {"q2"},
            ("q2", "0"): {"q2"},
            ("q2", "1"): {"q2"},
        },
        start="q0",
        finals={"q2"},
    )
