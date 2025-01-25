# Duplicate letter checker Create a function in Python that accepts one parameter: a string that’s a sentence. This
# function should return True if any word in that sentence contains duplicate letters and False if not.
import string


def duplicate_letter(s: str) -> bool:
    return len(s) != len(set(s))


res = duplicate_letter('abc')
print(res)

