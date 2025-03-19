def totalMoney(self, n: int) -> int:
        week = n // 7
        days = n % 7
        total = 28 * week
        for w in range(1, week):
            total += 7 * w
        for d in range(1, days+1):
            total += (week + d)
        return total
