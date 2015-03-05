def count_zero_pairs(numbers):
    pairs = []
    first_count = 0
    while first_count < len(numbers):
        second_count = first_count
        while second_count < len(numbers):
            if numbers[first_count] + numbers[second_count] == 0:
                pairs = pairs + [numbers[first_count]] + [numbers[second_count]]
            second_count = second_count + 1
        first_count = first_count + 1
    return pairs

numbers = [0, 2, -2, 5, 10]
items = count_zero_pairs(numbers)
print(items)
            
