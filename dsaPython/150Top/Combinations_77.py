import itertools
from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    return list(itertools.combinations(range(1, n + 1), k))


print(combine(4, 2))
