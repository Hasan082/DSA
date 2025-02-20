from typing import List
def findDifferentBinaryString(nums: List[str]) -> str:
    return "".join("1" if nums[i][i] == "0" else "0" for i in range(len(nums)))


print(findDifferentBinaryString(["01","10"])) # 11
print(findDifferentBinaryString(["00","01"])) # 10
print(findDifferentBinaryString(["111","011","001"])) # 101
print(findDifferentBinaryString(["111","011","101"])) # 010 