from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first_word, last_word = strs[0], strs[-1]
        res = ''
        for i in range(min(len(first_word), len(last_word))):
            if first_word[i] == last_word[i]:
                res += last_word[i]
            else:
                return res

        return res


result = Solution()
print(result.longestCommonPrefix(["flower", "flow", "flight"])) # 'fl'
print(result.longestCommonPrefix(["dog", "racecar", "car"])) # ''
