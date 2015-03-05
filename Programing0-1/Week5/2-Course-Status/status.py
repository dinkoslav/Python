def status_count(students):
    dict = {
            "finalized": [],
            "not_finalized": []
        }

    for student in students:
        if student["status"] == "finalized":
            dict["finalized"] = dict["finalized"] + [student["name"]]
        else:
            dict["not_finalized"] = dict["not_finalized"] + [student["name"]]

    return dict

students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }]

result = status_count(students)
print(result)
