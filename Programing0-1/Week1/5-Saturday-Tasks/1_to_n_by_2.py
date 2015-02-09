a = input("Enter a number to end with: ")
start = 1
a = int(a)

while start <= a:
    if start % 2 != 0:
        print(start)
    start = start + 1
