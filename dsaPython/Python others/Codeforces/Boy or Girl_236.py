# https://codeforces.com/problemset/problem/236/A

s = input()
unique_s = set(s)
if len(unique_s) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")