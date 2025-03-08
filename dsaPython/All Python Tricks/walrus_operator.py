# walrus Operator Tricks

# ========= TRICKS ONE=================
# Nomra way
while True:
    num = input("Enter a vald Number: ")

    if not num.isdigit():
        print("You Put something else rather than a valid number")
    else:
        print(f"you put {num}")
        break



#Using warles Operator
while not (num := input("Enter a vald Number: ")).isdigit():
    print("You Put something else rather than a valid number")


print(f"you put {num} using warles")