def secondHighest(s: str) -> int:
    res = []
    for c in s:
        if c.isdigit() and int(c) not in res:
            res.append(int(c))
    res.sort()
    return res[-2] if len(res) > 1 else -1