# https://codeforces.com/problemset/problem/2067/C

from collections import deque

def min_operations_to_seven(n):
    if '7' in str(n):  # Already contains '7'
        return 0

    queue = deque([(n, 0)])  # (current_number, step_count)
    visited = set()  # To avoid repeating numbers

    while queue:
        curr, steps = queue.popleft()

        for add_value in [9, 99, 999, 9999, 99999]:  # We can add different '9' values
            new_num = curr + add_value
            if '7' in str(new_num):
                return steps + 1  # We found the answer
            if new_num not in visited:  # Avoid cycles
                visited.add(new_num)
                queue.append((new_num, steps + 1))

    return -1  # Should never happen

# Read input
t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Read each test case
    print(min_operations_to_seven(n))



