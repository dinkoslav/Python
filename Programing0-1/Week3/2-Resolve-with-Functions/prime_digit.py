n = input("Enter n: ")
n = int(n)

def is_prime(n):
    count = 2
    is_prime = True
    while count <= number/2:
        if number % count == 0:
            is_prime = False
            break
        count = count + 1
    if n != 1 and n != 2:
        return is_prime
    else:
        return False

def to_digits(n):
    digits = []
    while n != 0:
        digit = n % 10
        digits = [digit] + digits
        n = n // 10
    return digits

numbers = to_digits(n)
prime_numbers = []
for number in numbers:
    if is_prime(number):
        prime_numbers = prime_numbers + [number]

print(prime_numbers)
