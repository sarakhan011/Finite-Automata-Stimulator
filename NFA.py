class NFA:
    def __init__(self, states, alphabet, transitions, start, finals):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.finals = finals

    def epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            for nxt in self.transitions.get((state, EPSILON), ()):
                if nxt not in closure:
                    closure.add(nxt)
                    stack.append(nxt)
        return frozenset(closure)

    def move(self, states, symbol):
        result = set()
        for state in states:
            result |= self.transitions.get((state, symbol), set())
        return result

    def run(self, string):
        """Return (path_of_state_sets, accepted)."""
        current = self.epsilon_closure({self.start})
        path = [current]
        for ch in string:
            current = self.epsilon_closure(self.move(current, ch))
            path.append(current)
            if not current:
                break 
        accepted = bool(path[-1] & self.finals)
        return path, accepted

    def accepts(self, string):
        return self.run(string)[1]
