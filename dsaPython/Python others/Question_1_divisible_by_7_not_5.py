# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).

def divisible_by_7(start, end):
    res = []
    for num in range(start, end+1):
        if num % 7 == 0 and num % 5 != 0:
            res.append(str(num))
    print(", ".join(res))


divisible_by_7(2000, 3000)

