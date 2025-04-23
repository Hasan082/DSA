from collections import Counter

target = Counter([0, 1, 0, 3, 2, 0, 2, 5])  # 01032025

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = Counter()
    answer = 0

    for i in range(n):
        cnt[arr[i]] += 1
        if all(cnt[d] >= target[d] for d in target):
            answer = i + 1
            break

    print(answer)
