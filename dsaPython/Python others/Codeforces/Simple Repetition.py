import sys
input = sys.stdin.readline

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
 

t = int(input())           

for _ in range(t):
    x, y = input().split()
    y = int(y)
    if len(x) * y > 18: 
        print("NO")
    else:
        whole = int(x * y)
        print("YES" if is_prime(whole) else "NO")
        
    


