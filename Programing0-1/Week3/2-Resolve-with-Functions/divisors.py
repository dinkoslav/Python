n = input("Enter n: ")
n = int(n)

def divisors(n):
    count = 1
    devisors = []
    while count <= n/2:
        if n % count == 0:
            devisors = devisors + [count]
        count = count + 1
    return devisors

print(divisors(n))
