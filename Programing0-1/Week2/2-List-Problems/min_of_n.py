n = input("Enter n: ")
n = int(n)

count = 1
min = 0

while count <= n:
    input_number = input()
    input_number = int(input_number)
    if count == 1:
        min = input_number
    else:
        if input_number < min:
            min = input_number
    count = count + 1

print("Min is: " + str(min))
