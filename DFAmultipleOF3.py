def example_dfa_multiple_of_3():
    """DFA over {0,1} accepting binary strings whose value is a multiple of 3."""
 
    return DFA(
        states={"q0", "q1", "q2"},
        alphabet={"0", "1"},
        transitions={
            ("q0", "0"): "q0", ("q0", "1"): "q1",
            ("q1", "0"): "q2", ("q1", "1"): "q0",
            ("q2", "0"): "q1", ("q2", "1"): "q2",
        },
        start="q0",
        finals={"q0"},
    )
