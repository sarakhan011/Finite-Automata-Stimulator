def format_dfa_path(path):
    return " → ".join(path)


def format_nfa_path(path):
    def fmt(s):
        return "{" + ",".join(sorted(s)) + "}" if s else "∅"
    return " → ".join(fmt(s) for s in path)


def show_result(automaton, string):
    path, accepted = automaton.run(string)
    trace = format_nfa_path(path) if isinstance(automaton, NFA) else format_dfa_path(path)
    print(trace)
    print(f"String: {string}")
    print(f"Result: {'ACCEPTED' if accepted else 'REJECTED'}")
    print()
