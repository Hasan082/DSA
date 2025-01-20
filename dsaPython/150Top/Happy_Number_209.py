class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        elif n < 10:
            return False
        t_sum = 0
        while n > 0:
            digit = n % 10
            t_sum += digit ** 2
            n //= 10
        return self.isHappy(t_sum)



