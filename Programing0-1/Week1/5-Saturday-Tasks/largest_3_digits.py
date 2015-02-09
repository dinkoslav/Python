n = input("Enter a 3-digit number: ")
n = int(n)

a = n % 10
n = n // 10

b = n % 10
n = n // 10

c = n % 10
n = n // 10

if b >= a and b >= c:
    if a > c:
        print(str(b) + str(a) + str(c))
    else:
        print(str(b) + str(c) + str(a))
elif c >= a and c >= b:
    if a > b:
        print(str(c) + str(a) + str(b))
    else:
        print(str(c) + str(b) + str(a))
else:
    if c > b:
        print(str(a) + str(c) + str(b))
    else:
        print(str(a) + str(b) + str(c))
