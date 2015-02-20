n = input("Enter n: ")
n = int(n)

count = 1
sum = 0

while count <= n/2:
    if n % count == 0:
        sum = sum + count
    count = count + 1

print(sum)
