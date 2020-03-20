from map_mover import (get_position_attractiveness_by_position)
from state import State


def test_get_element_index():
    array = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    s = State(array)

    assert s.get_element_index(5) == (1, 1)
    assert s.get_element_index(6) == (1, 2)
    assert s.get_element_index(8) == (2, 1)
    assert s.get_element_index(9) == (2, 2)


def test_swap_digits():
    array = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    s = State(array)

    assert s.swap_digits(1, 3).data == [
        [3, 2, 1],
        [4, 5, 6],
        [7, 8, 9]]

    assert s.swap_digits(9, 2).data == [
        [1, 9, 3],
        [4, 5, 6],
        [7, 8, 2]]

    assert s.swap_digits(6, 7).data == [
        [1, 2, 3],
        [4, 5, 7],
        [6, 8, 9]]


def test_get_position_attractiveness_by_position():
    array = [
        [1, 2, 6],
        [4, 5, 3],
        [7, 8, -1]]

    state = State(array)
    assert get_position_attractiveness_by_position(state) == 1 / 3

    array = [
        [3, 2, 1],
        [8, 6, 4],
        [7, -1, 5]]

    state = State(array)
    assert get_position_attractiveness_by_position(state) == 4 / 9


if __name__ == '__main__':
    test_get_element_index()
    test_swap_digits()
    test_get_position_attractiveness_by_position()
