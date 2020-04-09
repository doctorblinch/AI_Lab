from copy import deepcopy

GOAL_QUANTITY = 6
MAX_TABU_LIST_SIZE = 20


class State:
    def __init__(self, tabu_list=[], data=(-1, -1, -1)):
        self.tabu_list = tabu_list
        self._5 = data[0]
        self._7 = data[1]
        self._12 = data[2]
        self.metrics = abs(0 - self._5) / 5 + abs(6 - self._7) / 7 + abs(6 - self._12) / 12

    def __repr__(self):
        return "State({}, {}, {})\n".format(str(self._5), str(self._7), str(self._12))

    def __eq__(self, other):
        if isinstance(other, State):
            return (self._5 == other._5) and (self._7 == other._7) and (self._12 == other._12)

        return False

    def check_optimum(self) -> bool:
        if self._7 == GOAL_QUANTITY and self._12 == GOAL_QUANTITY:
            return True

        return False

    def get_possible_steps(self) -> list:
        jar5, jar7, jar12 = self._5, self._7, self._12
        possible_steps = []

        # Operations with jar5
        # Pure water from 5 jar to 7 jar
        if jar5 + jar7 > 7:
            possible_steps.append((jar5 + jar7 - 7, 7, jar12))
        else:
            possible_steps.append((0, jar5 + jar7, jar12))

        # Pure water from 7 jar to 5 jar
        if jar5 + jar7 > 5:
            possible_steps.append((5, jar5 + jar7 - 5, jar12))
        else:
            possible_steps.append((jar5 + jar7, 0, jar12))

        # Pure water from 5 jar to 12 jar
        if jar5 + jar12 > 12:
            possible_steps.append((jar5 + jar12 - 12, jar7, 12))
        else:
            possible_steps.append((0, jar7, jar5 + jar12))

        # Pure water from 12 jar to 5 jar
        if jar5 + jar12 > 5:
            possible_steps.append((5, jar7, jar5 + jar12 - 5))
        else:
            possible_steps.append((jar5 + jar12, jar7, 0))

        # Operations with jar7
        # Pure water from 7 jar to 12 jar
        if jar7 + jar12 > 12:
            possible_steps.append((jar5, jar7 + jar12 - 12, 12))
        else:
            possible_steps.append((jar5, 0, jar7 + jar12))

        # Pure water from 12 jar to 7 jar
        if jar7 + jar12 > 7:
            possible_steps.append((jar5, 7, jar7 + jar12 - 7))
        else:
            possible_steps.append((jar5, jar7 + jar12, 0))

        new_tabu = deepcopy(self.tabu_list)
        new_tabu.append(self)
        if len(new_tabu) > MAX_TABU_LIST_SIZE:
            new_tabu.pop(0)

        self.tabu_list = new_tabu

        removed_duplicates = []
        for step in list(set(possible_steps)):
            can_add = True
            for tabu in new_tabu:
                if step == (tabu._5, tabu._7, tabu._12):
                    can_add = False
                    break
            if can_add:
                removed_duplicates.append(State(data=step, tabu_list=new_tabu))

        return removed_duplicates
