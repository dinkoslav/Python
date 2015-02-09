a = input("Enter a number to end with: ")
start = 1
a = int(a)
sum = 0

while start <= a:
    if start % 2 != 0:
        print(start)
        sum = sum + start
    start = start + 1
print(sum)
