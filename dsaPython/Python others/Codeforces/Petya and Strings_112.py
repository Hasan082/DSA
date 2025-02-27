# https://codeforces.com/problemset/problem/112/A

a, b = input().lower(), input().lower()

if a < b:
    print(-1)
elif a > b:
    print(1)
else:
    print(0)