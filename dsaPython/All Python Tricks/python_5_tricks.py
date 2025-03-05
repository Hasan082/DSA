# Slice trick

numbers: list[int] = list(range(1, 11))
text: str = 'Hello, World!'
rev: slice = slice(None, None, -1) # Similar to [::-1]
f_five: slice = slice(None, -5)


print(numbers[rev])
print(text[rev])
print(numbers[f_five])
print(text[f_five])
# SIMILAR TO BELOW
print(numbers[::-1])
print(text[::-1])

