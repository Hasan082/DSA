from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    rns, mgz = Counter(ransomNote), Counter(magazine)
    for ch, counter in rns.items():
        if mgz[ch] < counter:
            return False
    return True


ransomNote1 = "a"
magazine1 = "b"
print(canConstruct(ransomNote1, magazine1))  # False
ransomNote2 = "aa"
magazine2 = "ab"
print(canConstruct(ransomNote2, magazine2))  # False
ransomNote3 = "aa"
magazine3 = "aab"
print(canConstruct(ransomNote3, magazine3))  # True
