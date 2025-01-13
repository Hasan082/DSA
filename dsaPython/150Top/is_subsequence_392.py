class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_iter = iter(t)
        return all(ch in t_iter for ch in s)


res = Solution()
print(res.isSubsequence("abc", "ahbgdc"))  # True
print(res.isSubsequence("axc", "ahbgdc"))  # False
