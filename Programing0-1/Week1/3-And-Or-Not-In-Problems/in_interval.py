a = input("Enter low limit: ")
b = input("Enter hi limit: ")
x = input("Enter number: ")

a = int(a)
b = int(b)
x = int(x)

if a == x:
    print("The number is equal to the lower bound of the interval")
elif b == x:
    print("The number is equal to the upper bound of the interval")
elif а < x < b:
    print("The number is in the interval")
elif x < a:
    print("The number is outside the interval, x < a")
elif x > b:
    print("The number is outside the interval, x > b")
