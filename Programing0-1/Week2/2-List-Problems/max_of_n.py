n = input("Enter n: ")
n = int(n)

count = 1
max = 0

while count <= n:
    input_number = input()
    input_number = int(input_number)
    if count == 1:
        max = input_number
    else:
        if input_number > max:
            max = input_number
    count = count + 1

print("Max is: " + str(max))
