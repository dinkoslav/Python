n = input("Enter a number: ")
n = int(n)
start = 2
is_prime = True

while start < n:
    if n % start == 0:
        print("The number is not prime!")
        is_prime = False
        break
    start = start + 1

if is_prime == True:
    print("The number is prime!")
