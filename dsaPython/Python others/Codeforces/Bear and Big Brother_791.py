# https://codeforces.com/problemset/problem/791/A

l, b = map(int, input().split())
years = 0
while l <= b:
    l *= 3
    b *= 2
    years +=1

print(years)
