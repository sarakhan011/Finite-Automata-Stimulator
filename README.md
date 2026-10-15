# Finite Automata Stimulator

A small, dependency-free Python program that simulates **DFAs** (Deterministic Finite Automata) and **NFAs** (Nondeterministic Finite Automata, including **ε-transitions**). It prints the full path of states for every input string and tells you whether the string is **ACCEPTED** or **REJECTED**.

- Runs a demo immediately, then offers an optional interactive menu


### Sample output

# DEMO 1: DFA — accepts binary strings ending in 1

q0 → q1 → q0 → q1 → q0 → q1
String: 10101
Result: ACCEPTED

q0 → q1 → q0 → q0 → q0
String: 1000
Result: REJECTED


# DEMO 2: NFA — accepts strings containing substring '01'

{q0} → {q0} → {q0} → {q0,q1} → {q0,q2}
String: 1101
Result: ACCEPTED

{q0} → {q0} → {q0} → {q0} → {q0,q1}
String: 1110
Result: REJECTED


For a DFA the trace is one state per step. For an NFA the trace is the **set of active states** per step (`∅` means every branch died).



## Built-in example automata

In every diagram, the arrow from nowhere marks the start state and a double circle marks an accepting state.

### 1. DFA: binary strings ending in `1`

![DFA ends in 1](images/dfa_ends_in_1.svg)

### 2. DFA: binary value is a multiple of 3

Each state stores the value read so far modulo 3 (`q0` = 0, `q1` = 1, `q2` = 2).

![DFA multiple of 3](images/dfa_multiple_of_3.svg)

### 3. NFA: contains the substring `01`

`q0` guesses when the `01` starts: on reading `0` it goes to both `q0` and `q1`.

![NFA contains 01](images/nfa_contains_01.svg)

### 4. NFA with ε-transition: only `a`s or only `b`s

From `q0` the machine can move to `q1` for free (ε) and then loop on `a`, or read `b` and loop in `q2`. Accepted strings: `a*` or `b*` (including the empty string).

![NFA epsilon](images/nfa_epsilon.svg)



## Further reading

See [DOCUMENTATION.md](DOCUMENTATION.md) for the class reference, algorithms, and how to add your own automata to the menu.
