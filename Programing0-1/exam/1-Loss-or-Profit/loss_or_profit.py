def loss_or_profit(income, outcome):
    total_income = sum_elements(income)
    total_outcome = sum_elements(outcome)

    difference = total_income - total_outcome

    if difference == 0:
        return "=0"
    elif difference > 0:
        return "+" + str(difference)
    else:
        return difference

def sum_elements(arr):
    result = 0
    for e in range(0, len(arr)):
        result += arr[e]
        
    return result

print(loss_or_profit([1, 2, 3], [3]))
print(loss_or_profit([10], [20, 30]))
print(loss_or_profit([10], [10]))
