t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    ones = s.count('1')
    zeros = n - ones

    max_pairs = n // 2
    min_pairs = abs(ones - zeros) // 2

    if min_pairs <= k <= max_pairs and (k - min_pairs) % 2 == 0:
        print("YES")
    else:
        print("NO")

