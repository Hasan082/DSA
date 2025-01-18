class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        arr = []

        matching_bracket = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in matching_bracket.values():  # mean it is opening bracket
                arr.append(ch)
            else:
                if not arr or arr[-1] != matching_bracket.get(ch):
                    return False
                arr.pop()

        return len(arr) == 0


sol = Solution()

print(sol.isValid("()[]{}"))  # Output: True
print(sol.isValid("([)]"))    # Output: False
print(sol.isValid("{[]}"))    # Output: True
