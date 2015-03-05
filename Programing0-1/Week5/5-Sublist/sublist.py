def sublist(list1, list2):
    if len(list1) == 0:
        return True

    count = 0
    while count <= len(list2) - len(list1):
        inner_count = 0
        is_sublist = True
        while inner_count < len(list1):
            if list1[inner_count] != list2[count + inner_count]:
                is_sublist = False
            inner_count = inner_count + 1
        if is_sublist == True:
            return True
        count = count + 1
        
    return False

# list1 = [1, 2, 3]
# list2 = [0, 0, 1, 2, 3, 5, 6]

# list1 = ["Python"]
# list2 = ["Python", "Django"]

# list1 = ["Python", "Django"]
# list2 = ["Django", "Python"]

list1 = [1,2]
list2 = [1, 0, 1, 2, 2]

print(sublist(list1, list2))
