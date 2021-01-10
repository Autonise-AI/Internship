# u have a list of 0,1,2's you have to sort it in-place without inbuilt command
N = int(input("give size: "))
lst = []
for i in range(N):
    x = int(input("give number: "))
    lst.append(x)
print(lst)
c0 = 0
c1 = 0
c2 = 0
for i in lst:
    if i == 0:
        c0 = c0+1
    elif i == 1:
        c1 = c1+1
    else:
        c2 = c2+1
n = len(lst)
for i in range(c0):
    lst[i] = 0
for i in range(c0, c0+c1):
    lst[i] = 1
for i in range(c0+c1, n):
    lst[i] = 2
print(lst)
