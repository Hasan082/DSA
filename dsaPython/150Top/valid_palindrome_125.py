class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "".join(filter(str.isalnum, s.lower()))
        return newStr == newStr[::-1]


res = Solution()
print(res.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(res.isPalindrome("race a car"))  # False
