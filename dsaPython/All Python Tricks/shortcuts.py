# F String

name = "Tim"

z = f'Hello {name} {[1, 2, 3]}'
x = F'Hello {name} {[1, 2, 3]}'
print(z)
print(x)


# Unpacking

tup = (1, 2, 3, 4, 5)
lst = [1, 2, 3, 4, 5]
string = "hello"
dic = {'a': 1, "b": 2}
coords = [4, 5]

a, b, c, d, e = tup
print(a, b, c, d, e)
f, g, h, i, j = lst
print(f, g, h, i, j)
k, l, m, n, o = string
print(k, l, m, n, o)
p, q = dic.values()
print(p, q)
r, s = dic.keys()
print(r, s)
t, u = dic.items()
print(t, u)
x, y = coords
print(x, y)