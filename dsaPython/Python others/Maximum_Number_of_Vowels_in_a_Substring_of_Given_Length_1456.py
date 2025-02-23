def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    current_sum = sum(1 for char in s[:k] if char in vowels)
    max_count = current_sum
    for i in range(k, len(s)):
        if s[i] in vowels:
            current_sum += 1
        if s[i - k] in vowels:
            current_sum -= 1
        max_count = max(max_count, current_sum)
        if k == current_sum:
            return k
    return max_count


s1 = "abciiidef"
k1 = 3
print(maxVowels(s1, k1)) # 3
s2 = "aeiou"
k2 = 2
print(maxVowels(s2, k2)) # 2