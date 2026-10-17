def example_dfa_ends_in_1():
    """DFA over {0,1} accepting strings that end in 1."""
    return DFA(
        states={"q0", "q1"},
        alphabet={"0", "1"},
        transitions={
            ("q0", "0"): "q0",
            ("q0", "1"): "q1",
            ("q1", "0"): "q0",
            ("q1", "1"): "q1",
        },
        start="q0",
        finals={"q1"},
    )
