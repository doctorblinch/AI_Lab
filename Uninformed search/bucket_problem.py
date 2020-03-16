GOAL_QUANTITY = 3
FIRST_BUCKET_MAX = 5
SECOND_BUCKET_MAX = 9
DEPTH = 15


class Node:
    def __init__(self, parent=None, children=[], data=()):
        self.parent = parent
        self.children = children
        self.data = data

    def __repr__(self):
        return "Node({}, {})".format(str(self.data[0]), str(self.data[1]))

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.data == other.data

        return False


def check_optimum(node: Node) -> bool:
    if node.data[0] == GOAL_QUANTITY or node.data[1] == GOAL_QUANTITY:
        return True

    return False


def get_possible_steps(node: Node) -> list:
    bucket1, bucket2 = node.data[0], node.data[1]
    possible_steps = [
        (bucket1, 0),
        (0, bucket2)
    ]

    # Pure water from second bucket to first
    if bucket1 + bucket2 > FIRST_BUCKET_MAX:
        possible_steps.append((FIRST_BUCKET_MAX, bucket1 + bucket2 - FIRST_BUCKET_MAX))
    else:
        possible_steps.append((bucket1 + bucket2, 0))

    # Pure water from first bucket to second
    if bucket1 + bucket2 > SECOND_BUCKET_MAX:
        possible_steps.append((bucket1 + bucket2 - SECOND_BUCKET_MAX, SECOND_BUCKET_MAX))
    else:
        possible_steps.append((0, bucket1 + bucket2))

    possible_steps.append((bucket1, SECOND_BUCKET_MAX))
    possible_steps.append((FIRST_BUCKET_MAX, bucket2))

    # Removing duplicates and checking if new state != current state
    removed_duplicates = []
    [removed_duplicates.append(Node(parent=node, data=step, children=[]))
     for step in possible_steps
     if step not in removed_duplicates
     if check_if_not_repeat(node, step)
     ]

    for step in removed_duplicates:
        node.children.append(step)

    return removed_duplicates


def check_if_not_repeat(node: Node, value) -> bool:
    if node.data == value:
        return False
    elif node.parent is None:
        return True
    else:
        return check_if_not_repeat(node.parent, value)


def get_node_parent_history(node, history):
    if node.parent is None:
        history.insert(0, node)
        return history
    else:
        history.insert(0, node)
        return get_node_parent_history(node.parent, history)


def DLS(starting_node: Node, check_success, depth=DEPTH) -> list:
    answers = []
    if depth > 0 and check_success(starting_node):
        #print(DEPTH - depth, get_node_parent_history(starting_node, []))
        answers.append(starting_node)
    for step in get_possible_steps(starting_node):
        answers += DLS(step, check_success, depth - 1)

    return answers
