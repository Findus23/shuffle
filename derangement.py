from random import shuffle
from typing import List


def is_derangement(original: List, shuffled: List) -> bool:
    return not any([x == y for (x, y) in zip(original, shuffled)])


def get_derangement(people: List) -> List:
    while True:
        shuffled = people[:]  # make a copy
        shuffle(shuffled)
        if is_derangement(people, shuffled):
            return shuffled


def test():
    a = [1, 2, 3, 4]
    assert is_derangement(a, [2, 1, 4, 3])
    assert not is_derangement(a, [1, 2, 4, 3])
    assert not is_derangement(a, [1, 3, 4, 2])
    assert is_derangement(a, get_derangement(a))


test()
