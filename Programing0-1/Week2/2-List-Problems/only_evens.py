n = input("Enter n: ")
n = int(n)

count = 1
even_numbers = []

while count <= n:
    input_number = input()
    input_number = int(input_number)
    if input_number % 2 == 0:
        even_numbers = even_numbers + [input_number]
    count = count + 1

print("Count of evens: " + str(len(even_numbers)))
print("Evens are:")
for number in even_numbers:
    print(number)
        
