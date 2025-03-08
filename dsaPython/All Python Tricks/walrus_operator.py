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



