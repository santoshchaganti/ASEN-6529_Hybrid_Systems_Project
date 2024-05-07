class ProductAutomaton:
    def __init__(self, ts, dfa):
        self.ts = ts
        self.dfa = dfa
        self.states = [(ts_state, dfa_state) for ts_state in ts.states for dfa_state in dfa.states]
        self.transitions = self.create_transitions()

    def create_transitions(self):
        transitions = {}
        for (ts_state, dfa_state) in self.states:
            if ts_state in self.ts.transitions:
                transitions[(ts_state, dfa_state)] = []
                for ts_next_state in self.ts.transitions[ts_state]:
                    ts_label = self.ts.states[ts_next_state]
                    dfa_next_state = self.dfa.transition(dfa_state, ts_label)
                    if dfa_next_state:
                        transitions[(ts_state, dfa_state)].append((ts_next_state, dfa_next_state))
        return transitions

def create_product_automaton(ts, dfa):
    return ProductAutomaton(ts, dfa)
