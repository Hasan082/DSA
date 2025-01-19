def lengthOfLongestSubstring(s: str) -> int:
    ms = set()
    l, ml = 0, 0
    for r in range(len(s)):
        while s[r] in ms:
            ms.remove(s[l])
            l += 1
        ms.add(s[r])
        if ml < r - l + 1:
            ml = r - l + 1
    return ml


print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))  # 1
print(lengthOfLongestSubstring("pwwkew"))  # 3
