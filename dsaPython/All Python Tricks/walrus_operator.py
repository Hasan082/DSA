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



#  Input Validation (Simple)

while (name := input("Enter your name (min 3 characters): ")).strip() and len(name) < 3:
    print("Name too short. Try again.")

print(f"Welcome, {name}!")


# List Filtering with Condition

data = ["123", "abc", "456", "789", "xyz", "0"]

numbers = [int(num) for item in data if (num := item).isdigit()]
print(numbers)



# Counting Elements in a Loop

import random

values = [random.randint(1, 10) for _ in range(20)]
count = sum(1 for value in values if (result := value) % 2 == 0)
print("count: ", values)
print("count: ", count)