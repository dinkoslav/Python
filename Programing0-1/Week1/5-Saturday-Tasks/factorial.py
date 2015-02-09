n = input("Enter a number: ")
n = int(n)

start_n = n
sum = 1

if n != 0:
    while n > 0:
        sum = sum * n
        n = n - 1
print(str(start_n) + "! = " + str(sum))
