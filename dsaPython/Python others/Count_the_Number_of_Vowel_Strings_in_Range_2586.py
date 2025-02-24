from typing import List
def vowelStrings(words: List[str], left: int, right: int) -> int:
    vowel = set('aeiou')
    return sum({c[0],c[-1]}.issubset(vowel) for c in words[left: right + 1])