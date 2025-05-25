
import sys

t, total = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()
count, left, right = 0, 0, len(lst) - 1
while left <= right:
    if lst[left] + lst[right] <= total:
        count += 1
    left += 1
    right -= 1

print(count)