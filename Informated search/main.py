from map_mover import *


if __name__ == '__main__':
    print('Starting position:')
    state = State(STARTING_POSITION)
    state.beautiful_print_position()
    print('Goal position:')
    State(GOAL_POSITION).beautiful_print_position()
    print('\n\nStarting algorithm:\n\n')

    final, _ = RBFS(state, print_each_state=True)
    final.beautiful_print_position()