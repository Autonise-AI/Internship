# x = {1: "monday", 2: "tuesday"}
# print(type(x))
# print(x)
# dict is mutable

x = {}
x[1] = "monday"
x[2] = "tuesday"
print(x)

# for i in x:
#     print(i)

for i in x.items():
    print(i)

# similar to contains method in java/c++
if 3 in x:
    print("yes")
else:
    print("no")
