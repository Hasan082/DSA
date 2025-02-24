from typing import List
def maximumValue(strs: List[str]) -> int:
    return max(int(c) if c.isdigit() else len(c) for c in strs)