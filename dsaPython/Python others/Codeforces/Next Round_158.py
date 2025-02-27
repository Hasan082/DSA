# https://codeforces.com/problemset/problem/158/A
a, b = map(int, input().split())
score = list(map(int, input().split()))
target = score[b - 1]
count = 0
for i in score:
    if i >=target and i > 0:
        count += 1

print(count)