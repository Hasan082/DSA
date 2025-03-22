from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char = [0] * 26

    for i in range(len(s)):
        char[ord(s[i]) - 97] += 1
        char[ord(t[i]) - 97] -= 1

    for c in char:
        if c != 0:
            return False

    return True


print(isAnagram("adc", "cba"))


# AlterNate solution
def isAnagram_alternate(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


print(isAnagram_alternate("abc", "cba"))