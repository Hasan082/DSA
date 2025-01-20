def wordPattern(pattern: str, s: str) -> bool:
    t = s.split()
    if len(t) != len(pattern):
        return False
    return len(set(zip(t, pattern))) == len(set(t)) == len(set(pattern))


p1 = "abba"
s1 = "dog cat cat dog"
print(wordPattern(p1, s1)) # True
