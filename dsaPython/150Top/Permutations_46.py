from typing import List
import itertools


def permute(nums: List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums))
