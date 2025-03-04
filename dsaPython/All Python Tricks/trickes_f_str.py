# TRICKS 1
n: int = 1_000_000_000
print(n)
n : int = 1000000000
print(f"{n:_}") # separated by underscore
print(f"{n:,}") # separted by coma(,)



# TRICKS 2

var: str = 'abc'

print(f"{var:>20}:") # make space before 
print(f"{var:<20}:") # make space after 
print(f"{var:^20}:") # make both side and text is middle


# TRICKS 3 DATETIME
from datetime import datetime

now: datetime = datetime.now()

print(f"{now:%d.%m.%y}") # 'y' Year is short form like 04.03.25
print(f"{now:%d.%m.%Y}") # by 'Y' Year is Full form form like 04.03.2025
print(f"{now:%d.%m.%Y (%H.%M.%S)}") # by '(%H.%M.%S)' Hour minute sec
print(f"{now:%c}") # Full Specification about date
print(f"{now:%I%p}") # Date and TIME AM/PM formate

