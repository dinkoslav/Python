n = input("Enter n: ")
n = int(n)

count = 1
sum = 0

while count <= n:
    input_number = input()
    input_number = int(input_number)
    sum = sum + input_number
    count = count + 1

print("The sum is:  " + str(sum))
        
