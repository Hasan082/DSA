from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        checkString = lambda x, y: y.startswith(x) and y.endswith(x)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if i != j and checkString(words[i], words[j]):
                    count += 1

        return count



s = Solution()
print(s.countPrefixSuffixPairs("abc"))
