# https://codeforces.com/problemset/problem/231/A

time_operation = int(input())
count = 0
for _ in range(time_operation):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        count += 1


print(count)