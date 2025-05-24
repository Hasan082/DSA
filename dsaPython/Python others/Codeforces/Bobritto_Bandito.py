# https://codeforces.com/contest/2094/problem/B

import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, m, l, r = map(int, sys.stdin.readline().rstrip('\n').split())
    if -l >= m:
        print(-m, 0)
    else:
        print(l, l + m)