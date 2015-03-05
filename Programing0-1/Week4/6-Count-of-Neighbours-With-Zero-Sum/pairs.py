def count_zero_neighbours(numbers):
    pairs = []
    count = 0
    while count < len(numbers) - 1:
        if numbers[count] + numbers[count+1] == 0:
            pairs = pairs + [numbers[count]]
            pairs = pairs + [numbers[count+1]]
        count = count + 1

    return pairs
    
numbers = [1, 2, -2, 0, 0, 5, -5]
pairs = count_zero_neighbours(numbers)
print(pairs)
