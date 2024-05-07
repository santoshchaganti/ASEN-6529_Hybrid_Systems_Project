from grid_world_env import GridWorld
from transition_system import TransitionSystem
from dfa import create_dfa
from product_automaton import create_product_automaton
from a_star import run_a_star

def main():
   
    grid_world = GridWorld()
    grid_world.show() 
    transition_system = TransitionSystem(grid_world.grid)
    dfa = create_dfa()
    product_automaton = create_product_automaton(transition_system, dfa)
    start_state = (('0,1'), 'q0')  
    goal_state = (('2,2'), 'q3')  

    
    path = run_a_star(product_automaton, start_state, goal_state)

    print("Path found:", path)

if __name__ == "__main__":
    main()
