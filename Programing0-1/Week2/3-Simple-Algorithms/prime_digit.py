n = input("Enter n: ")

count = 0
primes = []

while count < len(n):
    inner_count = 2
    is_prime = True
    number = int(n[count])
    while inner_count <= number/2:
        if number % inner_count == 0:
            is_prime = False
        inner_count = inner_count + 1
    count = count + 1
    if is_prime == True and number != 1 and number != 2:
        primes = primes + [number]

print(primes)
