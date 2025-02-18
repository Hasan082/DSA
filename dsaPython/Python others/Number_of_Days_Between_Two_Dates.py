from datetime import date
def daysBetweenDates(date1: str, date2: str) -> int:
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        d1 = date(y1, m1, d1)
        d2 = date(y2, m2, d2)        
        return abs((d2 - d1).days)


datex = "2019-06-29"
datey = "2019-06-30"
print(daysBetweenDates(datex, datey))