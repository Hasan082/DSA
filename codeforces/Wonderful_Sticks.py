N = int(input().strip())
for _ in range(N):
    l1 = int(input().strip())
    l2 = input().strip()

    first_digit = l1
    for i in range(l1 - 1):
        if l2[i] == '>':
            first_digit -= 1
    print(first_digit, end=" ")
    
    l, r = 1, 1
    for i in range(l1-1):
        if l2[i] == '<':
            print(first_digit - l, end=" ")
            l+=1
        else:
            print(first_digit + r, end=" ")
            r+=1
    print()




    
