n = input("Enter n: ")
n = int(n)

def is_prime(n):
    count = 2
    is_prime = True
    while count <= n/2:
        if n % count == 0:
            is_prime = False
            break
        count = count + 1
    if n != 1 and n != 2:
        return is_prime
    else:
        return False

if is_prime(n):
    print("Twin primes with " + str(n) + ":")
    if is_prime(n - 2):
        print(str(n - 2) + ", " + str(n))
    else:
        print(str(n - 2) + " is not")
    if is_prime(n + 2):
        print(str(n + 2) + ", " + str(n))
    else:
        print(str(n + 2) + " is not")
else:
    print(str(n) + " is not prime!")
