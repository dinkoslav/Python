def hash_them(keys, values):
    dict = {}
    count = 0
    for key in keys:
        if  count <= (len(values) - 1):
            dict[key] = values[count]
        else:
            dict[key] = "None"
        count = count + 1
    return dict
        
first_test = hash_them(["Ivan", "Maria"], [1, 2])
print(first_test)
second_test = hash_them(["Ivan", "Maria"], [1])
print(second_test)
