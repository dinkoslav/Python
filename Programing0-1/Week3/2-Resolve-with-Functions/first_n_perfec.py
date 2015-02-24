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



numbers = []
index = 1
while len(numbers) < n:
    if index == sum_ints(divisors(index)):
        numbers = numbers + [index]
    index = index + 1

print(numbers)
