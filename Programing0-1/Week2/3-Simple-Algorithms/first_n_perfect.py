n = input("Enter n: ")
n = int(n)

numbers = []
start_number = 1

while len(numbers) < n:
    sum = 0
    count = 1
    while count <= start_number/2:
        if start_number % count == 0:
            sum = sum + count
        count = count + 1
    if sum == start_number:
        numbers = numbers + [start_number]
    start_number = start_number + 1

for number in numbers:
    print(" - " + str(number))

# dont try with more than 4, it will load too much time
