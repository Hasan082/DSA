def containDuplicates_2(nums: list, k: int) -> bool:
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and abs(seen[num] - i) <= k:
            return True
        seen[num] = i
    return False


print(containDuplicates_2([1, 2, 3, 4, 2], 3))
