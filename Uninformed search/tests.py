from bucket_problem import (get_possible_steps, check_optimum, Node,
                            check_if_not_repeat, get_node_parent_history
                            )


def test_get_possible_steps():
    assert get_possible_steps(Node(data=(0, 0))) == [Node(data=(0, 9)), Node(data=(5, 0))]
    assert get_possible_steps(Node(data=(3, 4))) == [
        Node(data=(3, 0)), Node(data=(0, 4)), Node(data=(5, 2)),
        Node(data=(0, 7)), Node(data=(3, 9)), Node(data=(5, 4))
    ]


def test_check_optimum():
    assert check_optimum(Node(data=(3, 10)))
    assert not check_optimum(Node(data=(4, 5)))
    assert check_optimum(Node(data=(5, 3)))
    assert not check_optimum(Node(data=(8, 2)))
    assert check_optimum(Node(data=(3, 3)))


def test_check_if_not_repeat():
    a = Node(data=(0, 0))
    b = Node(data=(3, 0), parent=a)
    c = Node(data=(5, 4), parent=b)
    a.children = [b, c]
    b.children = [c]
    assert not check_if_not_repeat(c, (0, 0))
    assert check_if_not_repeat(c, (0, 3))
    assert not check_if_not_repeat(c, (5, 4))
    assert check_if_not_repeat(c, (5, 5))


def test_get_node_parent_history():
    a = Node(data=(0, 0))
    b = Node(data=(3, 0), parent=a)
    c = Node(data=(5, 4), parent=b)
    a.children = [b, c]
    b.children = [c]
    assert get_node_parent_history(c) == [a, b, c]


if __name__ == '__main__':
    test_get_possible_steps()
    test_check_optimum()
    test_check_if_not_repeat()
    test_get_node_parent_history()
