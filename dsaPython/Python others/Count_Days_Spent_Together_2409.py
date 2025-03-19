def convert_days(day: str, monthArra) -> int:
    month, day = map(int, day.split('-'))
    return sum(monthArra[:month-1]) + day


def countDaysTogether(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    startAlice = convert_days(arriveAlice, days_per_month)
    endAlice = convert_days(leaveAlice, days_per_month)
    startBob = convert_days(arriveBob, days_per_month)
    endBob = convert_days(leaveBob, days_per_month)

    startOverlap = max(startAlice, startBob)
    endOverlap = min(endAlice, endBob)

    return max(0, endOverlap - startOverlap + 1)


arriveAlice1 = "08-15"
leaveAlice1 = "08-18"
arriveBob1= "08-16"
leaveBob1 = "08-19"
print(countDaysTogether(arriveAlice1, leaveAlice1, arriveBob1, leaveBob1))
arriveAlice2 = "10-01"
leaveAlice2 = "10-31"
arriveBob2= "11-01"
leaveBob2 = "12-31"

print(countDaysTogether(arriveAlice2, leaveAlice2, arriveBob2, leaveBob2))
