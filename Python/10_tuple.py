x = ("alice", 20)
y = x
y = ("bob", 19)
print(x)
#tuple is immutable

x = (1, 2, 2, 4, 3)
print(x.index(3))
print(x.count(2))
# x.clear()
print(x)

p1 = (1, 2)
p2 = (4, 5)

e1 = (1, 2, 3)
e2 = (3, 4, 5)


def func(x, y):
    return (x+y, x*y)


p = func(2, 3)
print(type(p))
print(p[0])
print(p[1])
