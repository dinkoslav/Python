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

def sum_ints(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

if sum_ints(divisors(n)) == n:
    print("Its perfect")
else:
    print("Naah, its not perfect")

