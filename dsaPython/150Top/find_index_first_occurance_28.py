class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


res = Solution()
print(res.strStr("hello", "ll"))  # 2
print(res.strStr("leetcode", "leeto"))  # -1
print(res.strStr("sadbutsad", "sad"))  # 0
