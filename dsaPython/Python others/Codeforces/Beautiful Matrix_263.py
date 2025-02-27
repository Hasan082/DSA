# https://codeforces.com/problemset/problem/263/A

matrix = [[int(x) for x in input().split()] for _ in range(5)]
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 1:
            print(abs(2 - row) + abs(2 - col))
            break