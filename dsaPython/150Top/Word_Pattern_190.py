def wordPattern( pattern: str, s: str) -> bool:
    t = s.split()
    if len(t) != len(pattern):
        return False
    return len(set(zip(t, pattern))) == len(set(t)) == len(set(pattern))


pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s)) # True
