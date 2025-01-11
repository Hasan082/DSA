class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        roman, prev = 0, 0
        for ch in s[::-1]:
            cur = roman_numerals.get(ch)
            if cur < prev:
                roman -= cur
            else:
                roman += cur
            prev = cur
        return roman


res = Solution()
print(res.romanToInt('III'))  # 3
print(res.romanToInt('LVIII'))  # 58
print(res.romanToInt('MCMXCIV'))  # 1994
