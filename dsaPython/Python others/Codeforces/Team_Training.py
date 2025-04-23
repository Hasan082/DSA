# https://codeforces.com/contest/2091/problem/B
t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    skills = list(map(int, input().split()))
    skills.sort(reverse=True)
    count, members, = 0, 0
    for skill in skills:
        members += 1
        if members * skill >= x:
            count += 1
            members = 0

    print(count)
