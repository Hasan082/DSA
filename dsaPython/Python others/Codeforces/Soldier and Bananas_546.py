# https://codeforces.com/problemset/problem/546/A

k, n, w = map(int, input().split())
total = 0

for i in range(w):
    total += (i + 1) * k

print(total - n if total > n else 0)