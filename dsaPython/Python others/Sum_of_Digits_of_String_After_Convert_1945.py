def helper(numStr):
    return sum(int(d) for d in numStr)

def getLucky(s: str, k: int) -> int:
    num_str = "".join((str(ord(char) - 96) for char in s))
    for _ in range(k):
        num_str = str(helper(num_str))
    return int(num_str)


print(getLucky("iiii", 1)) # 36
print(getLucky("leetcode", 2)) # 6
print(getLucky("zbax", 2)) # 8