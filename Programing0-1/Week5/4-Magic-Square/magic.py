def magic_square(square):
    sum = 0
    for row in square:
        temp_sum = 0
        for number in row:
            temp_sum = temp_sum + number
        if sum == 0:
            sum = temp_sum
        if temp_sum != sum:
            return False

    count = 0
    while count < len(square):
        temp_sum = 0
        inner_count = 0
        while inner_count < len(square):
            temp_sum = temp_sum + square[inner_count][count]
            inner_count = inner_count + 1
        if temp_sum != sum:
            return False
        count = count + 1
        
    count = 0
    temp_sum = 0
    while count < len(square):
        temp_sum = temp_sum + square[count][count]
        count = count + 1
        
    if temp_sum != sum:
        return False

    count = 0
    temp_sum = 0
    while count < len(square):
        temp_sum = temp_sum + square[count][len(square) - count - 1]
        count = count + 1
        
    if temp_sum != sum:
        return False

    return True
    
square1 = [ [23, 28, 21], [22, 24, 26], [27, 20, 25] ]
square2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
print(magic_square(square1))
print(magic_square(square2))
