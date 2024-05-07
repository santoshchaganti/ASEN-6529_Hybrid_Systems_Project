class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def transition(self, current_state, input_symbol):
        return self.transition_function.get((current_state, input_symbol), None)

    def is_accepting(self, state):
        return state in self.accept_states

def create_dfa():
    states = ['q0', 'q1', 'q2', 'q3', 'q4'] 
    alphabet = ['Robot', 'Key', 'Letter', 'Deliver', 'Fire'] 

    transition_function = {
        ('q0', 'Fire'): 'q0',  
        ('q0', 'Key'): 'q1',  
        ('q1', 'Letter'): 'q2', 
        ('q2', 'Deliver'): 'q3',  
       
    }
    start_state = 'q0'
    accept_states = ['q3'] 

    return DFA(states, alphabet, transition_function, start_state, accept_states)
