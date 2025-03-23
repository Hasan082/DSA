from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    lst = sorted(count.items(), key=lambda x: x[1], reverse=True)
    res = []
    for n, f in lst[:k]:
        res.append(n)
    return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))
