# https://codeforces.com/contest/1883/problem/A
N = int(input().strip())
for _ in range(N):
    n = input().strip()
    ans = 10 if int(n[0]) == 0 else int(n[0])
    for i in range(len(n) - 1):
        ans += 1
        num1 = 10 if n[i] == '0' else int(n[i])
        num2 = 10 if n[i+1] == '0' else int(n[i+1]) 
        ans += abs(num1 - num2)
    print(ans)

    


