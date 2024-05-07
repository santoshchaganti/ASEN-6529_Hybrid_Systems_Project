from grid_world_env import GridWorld
from transition_system import TransitionSystem
from dfa import DFA
from product_automaton import ProductAutomaton
from q_learning import QLearning

def main():
    env = GridWorld()
    env.show()
    ts = TransitionSystem(env)
    dfa = DFA()
    pa = ProductAutomaton(ts, dfa, env.grid) 
    ql = QLearning(pa)
    ql.train(5000, 50)
    policy = ql.get_policy()

    current_state = (env.robot_position, 'q0')
    steps = 100 

    for _ in range(steps):
        if current_state in policy:
            next_state = policy[current_state]
            env.update_robot_position(next_state[0])
            env.show()
            current_state = next_state
            if dfa.is_accepting(next_state[1]):
                print("Goal reached!")
                break

if __name__ == "__main__":
    main()
