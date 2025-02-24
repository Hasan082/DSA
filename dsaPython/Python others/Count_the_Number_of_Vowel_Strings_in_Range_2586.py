from typing import List
def vowelStrings(words: List[str], left: int, right: int) -> int:
    vowel = set('aeiou')
    return sum({c[0],c[-1]}.issubset(vowel) for c in words[left: right + 1])


words1 = ["are","amy","u"]
left1 = 0
right1 = 2
print(vowelStrings(words1, left1, right1)) # 2
words2 = ["hey","aeo","mu","ooo","artro"]
left2 = 1
right2 = 4
print(vowelStrings(words2, left2, right2)) # 3