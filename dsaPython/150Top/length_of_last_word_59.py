class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.strip().split()
        return len(res[-1])


res = Solution()

print(res.lengthOfLastWord("Hello World"))  # 5
print(res.lengthOfLastWord("   fly me   to   the moon  "))  # 4
print(res.lengthOfLastWord("luffy is still joyboy"))  # 6
