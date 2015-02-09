n = input("Enter a number: ")
n = int(n)

normal_number = n
reversed_number = 0

while n != 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n = n // 10
if normal_number == reversed_number:
    print("The number is palindrom")
else:
    print("The number is not palindrom")
