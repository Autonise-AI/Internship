# lst = [23, 1, 41, -23, 55]

# print(type(lst))
# print(lst)
# lst.reverse()
# lst.sort()
# print(lst)  # reverse is method

# mutable object -> called by reference
# x = 0xxy232
x = [1, 2, 3]
# y = x # y is copying the reference
y = x.copy()  # creates a new address for y and places data there
y.reverse()
# print(x)

# a = 1
# b = a
# b = 2
# print(a)
# same behaviour for int,str,bool,float

lst = [23, 1, 41, -23, 55]
# lst.append(0)  # adding at the end
# print(lst)
# lst.pop(2)
# print(lst)

# operators
# print(lst[3])
# print(lst[-1])
# print(lst[:4])
print(lst[::-1])

s = "sunday"
print(s[::-1])
