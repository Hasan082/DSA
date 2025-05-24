import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = sys.stdin.readline().rstrip('\n')

    count = 0 
    trailing = True

    for ch in reversed(s):
        if ch == '0':
            count += 1
            if trailing:
                count -= 1
        else:
            trailing = False

    print(len(s) - count - 1)