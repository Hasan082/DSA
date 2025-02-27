# https://codeforces.com/problemset/problem/339/A

lst = list(map(int, input().split('+')))
lst.sort()
print('+'.join(map(str, lst)))