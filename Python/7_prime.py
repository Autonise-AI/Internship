def isPrime(x):
    if x == 0:
        return False
    if x == 2:
        return True
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    return True


# x = int(input("x = "))
# if isPrime(x):
#     print("prime")
# else:
#     print("not prime")


x = int(input("x = "))
for i in range(2, x):
    if isPrime(i):
        print(i)
