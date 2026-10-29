def example_nfa_with_epsilon():
    """NFA using an epsilon transition: accepts 'a' or any string of b's."""
    return NFA(
        states={"q0", "q1", "q2"},
        alphabet={"a", "b"},
        transitions={
            ("q0", EPSILON): {"q1"},
            ("q1", "a"): {"q1"},
            ("q0", "b"): {"q2"},
            ("q2", "b"): {"q2"},
        },
        start="q0",
        finals={"q1", "q2"},
    )
