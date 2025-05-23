# https://codeforces.com/contest/2094/problem/A
# A. Trippi Troppi

N = int(input().strip())

while N>0:
    N-=1

    name = input().strip().split()
    for i in range(len(name)):
        print(name[i][0], end="")
    print()


