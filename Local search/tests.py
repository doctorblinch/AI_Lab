from state import State


def test_state_possible_steps():
    s = State(data=(0, 0, 12))
    assert s.get_possible_steps() == [State(data=(5, 0, 7)), State(data=(0, 7, 5))]

    s = State(data=(4, 3, 5))
    assert s.get_possible_steps() == [State(data=(5, 3, 4)),
                                      State(data=(4, 7, 1)),
                                      State(data=(0, 7, 5)),
                                      State(data=(0, 3, 9)),
                                      State(data=(5, 2, 5)),
                                      State(data=(4, 0, 8))]


def test_state_check_optimum():
    s = State(data=(2, 4, 6))
    assert not s.check_optimum()

    s = State(data=(0, 6, 6))
    assert s.check_optimum()

    s = State(data=(0, 5, 7))
    assert not s.check_optimum()


def test_all():
    test_state_possible_steps()
    test_state_check_optimum()


if __name__ == '__main__':
    test_all()
