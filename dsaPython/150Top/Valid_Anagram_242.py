def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t): return False
    for char in set(s):
        if s.count(char) != t.count(char): return False
    return True


s1 = "anagram"
t1 = "nagaram"
print(isAnagram(s1, t1)) # True

s2 = "rat"
t2 = "car"
print(isAnagram(s2, t2)) # False
