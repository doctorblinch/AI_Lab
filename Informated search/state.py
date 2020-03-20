from copy import deepcopy


class State:
    def __init__(self, data, parent=None, children=None, depth=0, h_value=-1):
        if children is None:
            children = []
        self.parent = parent
        self.children = children
        self.data = deepcopy(data)
        if depth == 0 and parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = depth
        self.h_value = h_value

    def __repr__(self):
        return "State({})".format(self.data)

    def beautiful_print_position(self):
        print('\n'.join(['  '.join([str(cell) if cell != -1 else ' ' for cell in row]) for row in self.data]))

    def __eq__(self, other):
        if isinstance(other, State):
            return self.data == other.data

        return False

    def get_available_steps(self) -> list:
        available_steps = []

        # Looking from position of hole, presented by "-1"
        y, x = self.get_element_index(-1)

        # Step Up
        if y > 0:
            possible_step = self.swap_digits(-1, self.data[y - 1][x])
            if not possible_step.check_if_present_in_history():
                available_steps.append(possible_step)

        # Step down
        if y < len(self.data) - 1:
            possible_step = self.swap_digits(-1, self.data[y + 1][x])
            if not possible_step.check_if_present_in_history():
                available_steps.append(possible_step)

        # Step left
        if x > 0:
            possible_step = self.swap_digits(-1, self.data[y][x - 1])
            if not possible_step.check_if_present_in_history():
                available_steps.append(possible_step)

        # Step right
        if x < len(self.data[0]) - 1:
            possible_step = self.swap_digits(-1, self.data[y][x + 1])
            if not possible_step.check_if_present_in_history():
                available_steps.append(possible_step)

        self.children = available_steps
        return available_steps

    def get_element_index(self, element):
        for line in self.data:
            if element in line:
                return self.data.index(line), line.index(element)

    def swap_digits(self, element1, element2):
        position = State(deepcopy(self.data), self)

        y1, x1 = self.get_element_index(element1)
        y2, x2 = self.get_element_index(element2)

        position.data[y1][x1] = element2
        position.data[y2][x2] = element1

        return position

    def check_if_present_in_history(self, value=None) -> bool:
        if value is None:
            value = self.data
            return self.parent.check_if_present_in_history(value)

        if self.data == value:
            return True
        elif self.parent is None:
            return False
        else:
            return self.parent.check_if_present_in_history(value)


# from map_mover import *
# s = State(GOAL_POSITION)
# ss = s.get_available_steps()
# z = ss[0].get_available_steps()
# z[0].data = GOAL_POSITION
# z[0].check_if_present_in_history()
