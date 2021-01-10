# set can have only immutable objects stored
x = {1, 3, 5, 7}
print(type(x))
# print(x)
#set is mutable
# y = x
# y.clear()
# print(x)

x.add(9)
print(x)
x.add(7)
print(x)
x.discard(7)
print(x)

print(len(x))

x = {"1", "22", "3"}
print(x)

# y = {[1, 2, 3], [12, 5, 6]} throws error because list is mutable object
# print(y)
