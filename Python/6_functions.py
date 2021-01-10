def greet():
    # reusable
    print("hey!")
    print("hello")


def greet1():
    x = input("name : ")
    print("hello, ", x)


# greet1()
# greet1()
# x is an argument
def area(x):
    return x*x


# y = area(23)
# print(y)

def find(x):
    return (x**2, x**3)


(y, z) = find(23)
# print(y)
# print(z)

# inbuilt functions
# print(max(1, 2))
# print(abs(-23.2))

# global variable
x = 3


def monday():
    # local variable
    global x
    x = 25
    print("x = ", x)


x = monday()
print("x = ", x)
