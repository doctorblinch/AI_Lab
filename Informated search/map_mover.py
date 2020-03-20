from state import State

GOAL_POSITION = [
    [1, 2, 3],
    [-1, 8, 4],
    [7, 6, 5]
]

STARTING_POSITION = [
    [2, 8, 3],
    [1, 6, 4],
    [7, -1, 5]
]

H_LIMIT = 100_000


def check_optimum2(position: State) -> bool:
    return True if position.data == GOAL_POSITION else False


def check_optimum(position: State) -> bool:
    for i in range(len(position.data)):
        for j in range(len(position.data[0])):
            if position.data[i][j] != GOAL_POSITION[i][j]:
                return False

    return True


def get_position_attractiveness_by_position(position: State) -> float:
    # Shows how many of digits will be on their places
    attractiveness = 0
    for i in range(len(GOAL_POSITION)):
        for j in range(len(GOAL_POSITION[0])):
            if position.data[i][j] == GOAL_POSITION[i][j]:
                attractiveness += 1

    # Normalize
    return attractiveness / (len(position.data) * len(position.data[0]))


def print_all_states_with_heuristics(states: list, heuristic=get_position_attractiveness_by_position):
    print('\nQuantity of states {}\n\n{}'.format(len(states), '#' * 50))
    for state in states:
        state.beautiful_print_position()
        print('\nAttractiveness: ', heuristic(state))
        print('\n\n{}'.format('#' * 50))


def get_position_attractiveness_by_distance(position: State) -> float:
    # Shows distance between goal position and current position for each number
    distance = 0
    # For easier search in future
    s = State(GOAL_POSITION)

    for i in range(1, len(position.data) * len(position.data[0])):
        x, y = position.get_element_index(i)
        x_goal, y_goal = s.get_element_index(i)

        distance += (9 - abs(x - x_goal) - abs(y - y_goal)) / 9

    return distance


def RBFS(state: State, iteration=0, h_limit=H_LIMIT, history=[], print_each_state=False):

    if print_each_state:
        state.beautiful_print_position()
        print('\nHeuristics value: {}.\n\n{}\n'.format(get_position_attractiveness_by_position(state), '#'*50))

    if check_optimum(state):
        return state, None

    iteration += 1

    all_successors = state.get_available_steps()
    successors = []

    for successor in all_successors:
        if successor.data not in history:
            successors.append(successor)
            history.append(successor.data)

    if not successors:
        return None, H_LIMIT

    for s in successors:
        s.h_value = max(s.h_value, state.h_value)

    while successors:
        successors.sort(key=lambda x: x.h_value)
        best = successors[0]
        if best.h_value > h_limit:
            return None, best.h_value
        if len(successors) > 1:
            alternative = successors[1].h_value
        else:
            alternative = H_LIMIT
        result, best.h_value = RBFS(best, iteration, min(h_limit, alternative),
                                    history, print_each_state=print_each_state)
        if result is not None:
            return result, best.h_value
    return None, None
