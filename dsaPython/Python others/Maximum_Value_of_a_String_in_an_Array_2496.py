from typing import List
def maximumValue(strs: List[str]) -> int:
    return max(int(c) if c.isdigit() else len(c) for c in strs)


strs1 = ["alic3","bob","3","4","00000"]
print(maximumValue(strs1)) # 5
strs2 = ["1","01","001","0001"]
print(maximumValue(strs2)) # 1