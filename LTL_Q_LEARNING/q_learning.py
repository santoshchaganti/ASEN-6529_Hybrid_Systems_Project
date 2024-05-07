import numpy as np
import random

class QLearning:
    def __init__(self, automaton, learning_rate=0.1, discount_factor=0.95, epsilon=0.1):
        self.automaton = automaton
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_values = {state: {neighbor: 0 for neighbor in automaton.transitions[state]} for state in automaton.states}

    def train(self, episodes, steps_per_episode):
        for episode in range(episodes):
            state = random.choice(list(self.q_values.keys()))  
            for step in range(steps_per_episode):
                if random.uniform(0, 1) < self.epsilon: 
                    action = random.choice(list(self.q_values[state].keys()))
                else:
                    action = max(self.q_values[state], key=self.q_values[state].get)
                next_state = action
                reward = 100 if self.automaton.dfa.is_accepting(next_state[1]) else -1
                old_value = self.q_values[state][action]
                next_max = max(self.q_values[next_state].values(), default=0)
                new_value = old_value + self.learning_rate * (reward + self.discount_factor * next_max - old_value)
                self.q_values[state][action] = new_value
                state = next_state

                print(f"Episode {episode}, Step {step}: State {state}, Action {action}, Reward {reward}, Next State {next_state}")

    def get_policy(self):
        policy = {}
        for state in self.q_values:
            policy[state] = max(self.q_values[state], key=self.q_values[state].get)
        return policy
