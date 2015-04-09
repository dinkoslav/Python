def second_largest(numbers):
    sorted_numbers = sorted(numbers)
    sorted_numbers = sorted_numbers[::-1]

    have_second = False
    second_number = 0;

    if len(sorted_numbers) <= 1:
        return False
    else:
        first_number = sorted_numbers[0]
        for e in range(1, len(sorted_numbers)):
            if first_number != sorted_numbers[e]:
                have_second = True
                second_number = sorted_numbers[e]
                break
    if have_second:
        return second_number
    else:
        return have_second
    
print(second_largest([]))
print(second_largest([2, 1]))
print(second_largest([5, 5]))
print(second_largest([100, 100, 90]))
    
