from grid_world_env import GridWorld

class TransitionSystem:
    def __init__(self, grid_world):
        self.grid_world = grid_world
        self.grid = grid_world.grid
        self.states = self.generate_states()
        self.transitions = self.generate_transitions()

    def generate_states(self):
        states = []
        for r in range(self.grid.shape[0]):
            for c in range(self.grid.shape[1]):
                if self.grid[r, c] != "Fire":
                    states.append((r, c))
        return states

    def generate_transitions(self):
        transitions = {}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        for state in self.states:
            transitions[state] = {}
            for dr, dc in directions:
                next_state = (state[0] + dr, state[1] + dc)
                if next_state in self.states:
                    transitions[state][next_state] = 1 
        return transitions

    def get_neighbors(self, state):
        return self.transitions.get(state, {})