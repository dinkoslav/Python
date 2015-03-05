def get_people_count(activity):
    dict = {}
    for person in activity:
        if person in dict:
            dict[person] = dict[person] + 1
        else:
            dict[person] = 0
    return len(dict)

activity = ["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]
people_count = get_people_count(activity)
print(people_count)
