def run_demo():
    print("=" * 60)
    print("DEMO 1: DFA — accepts binary strings ending in 1")
    print("=" * 60)
    dfa = example_dfa_ends_in_1()
    show_result(dfa, "10101")   # ACCEPTED
    show_result(dfa, "1000")    # REJECTED

    print("=" * 60)
    print("DEMO 2: NFA — accepts strings containing substring '01'")
    print("=" * 60)
    nfa = example_nfa_contains_01()
    show_result(nfa, "1101")    # ACCEPTED
    show_result(nfa, "1110")    # REJECTE
