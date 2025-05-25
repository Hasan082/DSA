# https://codeforces.com/contest/2094/problem/A
# A. Trippi Troppi

N = int(input().strip())

for _ in range(N):
    name = input().strip().split()
    for i in range(len(name)):
        print(name[i][0], end="")
    print()


