def prime_pair(numbers):
    first_count = 0
    while first_count < len(numbers):
        second_count = first_count
        while second_count < len(numbers):
            sum = numbers[first_count] + numbers[second_count]
            if is_prime(sum):
                return True
            second_count = second_count + 1
        first_count = first_count + 1
    return False

def is_prime(number):
    if number <= 1:
        return False
    else:
        count = 2
        while count < number/2:
            if number % count == 0:
                return False
        return True

numbers = [1, 2, 3, 4, 5]
print(prime_pair(numbers))
