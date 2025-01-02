class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = s.strip().split()
        return len(r[-1])


res = Solution()

print(res.lengthOfLastWord("Hello World"))  # 5
print(res.lengthOfLastWord("   fly me   to   the moon  "))  # 4
print(res.lengthOfLastWord("luffy is still joyboy"))  # 6
