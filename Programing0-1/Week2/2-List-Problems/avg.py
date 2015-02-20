n = input("Enter n: ")
n = int(n)

count = 1
numbers = []
sum = 0

while count <= n:
    input_number = input()
    input_number = int(input_number)
    numbers = numbers + [input_number]
    count = count + 1

for number in numbers:
    sum = sum + number

avg = sum / len(numbers)
print("Avg is: " + str(avg))
