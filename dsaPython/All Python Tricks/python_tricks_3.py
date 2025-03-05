user: dict[int, str] = {
    0: 'Bob',
    1: 'Mario'
}

# user: str | None = user.get(3)

# if user:
#     print(f"{user} Exists")
# else:
#     print("User Not Found")

# Tricks for above 

if user := user.get(3): # := walrus operator
    print(f"{user} Exists")
else:
    print("User Not Found")