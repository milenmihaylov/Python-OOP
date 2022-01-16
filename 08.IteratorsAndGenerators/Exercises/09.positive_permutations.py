from itertools import permutations


def possible_permutations(ll: list):
    for p in permutations(ll):
        yield list(p)


[print(n) for n in possible_permutations([1, 2, 3])]
