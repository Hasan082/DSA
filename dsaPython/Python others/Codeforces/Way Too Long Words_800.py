# https://codeforces.com/problemset/problem/71/A


def encode_words(words: str) -> str:
    try:
        if len(words) > 10:
            return words[0] + str(len(words) - 2) + words[-1]
        else:
            return words
    except (ValueError, TypeError):
        print("Invalid Input")
        encode_words(words)

n = int(input())
for _ in range(n):
    print(encode_words(input()))