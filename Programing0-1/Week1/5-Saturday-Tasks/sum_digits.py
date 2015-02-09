n = input("Enter N: ")
m = input("Enter M: ")
n = int(n)
m = int(m)

while n <= m:
    sum = 0
    number = n
    while number != 0:
        digit = number % 10
        sum = sum + digit
        number = number // 10
    print("Sum of digits of " + str(n) + " = " + str(sum))
    n = n + 1
