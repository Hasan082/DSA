class Solution:
    def intToRoman(self, num: int) -> str:

        num_to_roman = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        roman = ''

        for value, symbol in num_to_roman:
            while num >= value:
                roman += symbol
                num -= value

        return roman


res = Solution()
print(res.intToRoman(3749))  # "MMMDCCXLIX"
print(res.intToRoman(58))  # LVIII
print(res.intToRoman(1994))  # MCMXCIV
