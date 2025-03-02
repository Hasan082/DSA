maps: dict = {
    1: 3,
    2 : 4,
    3: 5
}
nums = [5, 6, 7]
print(list(maps.values())[0])

# maps.items() -> key, ValueError
# maps.keys() -> KeyboardInterrupt
# maps.values() value

print(5 in maps)
