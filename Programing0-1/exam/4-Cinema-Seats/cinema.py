def order_of_seats(cinema):
    result = []
    counter = 0
    
    while counter < len(cinema):
        row = find_empty_seats_row(cinema)
        
        for c in range(0, len(cinema[row])):
            if cinema[row][c] == 0:
                seat = "(" + str(row + 1) + ", " + str(c + 1) + ")"
                result = result + [seat]
                cinema[row][c] = 1

        counter += 1
        
    return result
    
def sum_elements(arr):
    result = 0
    for e in range(0, len(arr)):
        result += arr[e]
        
    return result

def find_empty_seats_row(cinema):
    row = 0
    empty_seats = len(cinema[0]) + 1
    
    for r in range(0, len(cinema)):
        row_empty_seats = len(cinema[0]) - sum_elements(cinema[r])
        if  row_empty_seats != 0 and row_empty_seats <= len(cinema[0]) and row_empty_seats < empty_seats:
            row = r
            empty_seats = row_empty_seats

    
    return row
            
        
    
cinema1 = [ [0, 0],
           [0, 0],
           [0, 0] ]

cinema2 = [ [1, 1, 1],
           [1, 0, 0],
           [1, 0, 0],
           [1, 1, 0] ]

cinema3 = [ [1, 1, 1, 0],
           [1, 0, 1, 0],
           [0, 0, 0, 0],
         ]
#print(order_of_seats(cinema1))
#print(order_of_seats(cinema3))
print(order_of_seats(cinema2))
