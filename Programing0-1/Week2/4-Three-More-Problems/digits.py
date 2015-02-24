n = input("Enter n: ")
n = int(n)

digits = []

while n != 0:
    digit = n % 10
    digits = [digit] + digits
    n = n // 10

number = 0

for digit in digits:
    number = number * 10 + digit
    
print("List of digits is : " + str(digits))
print("Number is: " + str(number))
