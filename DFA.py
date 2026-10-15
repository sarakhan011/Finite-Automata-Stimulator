class DFA:
    def __init__(self, states, alphabet, transitions, start, finals):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions  
        self.start = start
        self.finals = finals

    def run(self, string):
        """Return (path_of_states, accepted). Stops early if stuck."""
        state = self.start
        path = [state]
        for ch in string:
            key = (state, ch)
            if key not in self.transitions:
                return path, False  
            state = self.transitions[key]
            path.append(state)
        return path, state in self.finals

    def accepts(self, string):
        return self.run(string)[1]
