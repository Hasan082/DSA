# https://codeforces.com/contest/2065/problem/A

t = int(input().strip())

while t > 0:
    s = input().strip()
    if s.endswith("us"):
        print(s[:-2] + "i")
    t-=1


