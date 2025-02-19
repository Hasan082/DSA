def xorOperation(n: int, start: int) -> int:
    res = 0
    for _ in range(n):
        res ^= start
        start = start + 2
    return res

n = 5
start = 0
print(xorOperation(n, start)) # 8

