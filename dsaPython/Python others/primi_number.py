def primi_number(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True


for num in range(1, 100):
    if primi_number(num):
        print(num, end=" ")