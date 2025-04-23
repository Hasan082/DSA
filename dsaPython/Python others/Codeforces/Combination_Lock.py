t = int(input())

for _ in range(t):
    n = int(input())
    arr = [str(i) for i in range(1, n + 1)]
    if n % 2 == 0:
        print(-1)
    else:
        print(" ".join(arr[::-1]))

            