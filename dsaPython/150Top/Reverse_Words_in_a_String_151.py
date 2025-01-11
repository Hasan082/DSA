class Solution:
    def reverseWords(self, s: str) -> str:
        newString = s.split()
        return " ".join(newString[::-1])


res = Solution()
print(res.reverseWords("the sky is blue"))  # Output: "blue is sky the"
print(res.reverseWords("  hello world  "))  # Output: "world hello"
print(res.reverseWords("a good   example"))  # Output: "example good a"
