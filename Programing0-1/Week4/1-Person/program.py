from datetime import date
currentYear = date.today().year

firstName = input("Enter first name: ")
secondName = input("Enter second name: ")
thirdName = input("Enter third  name: ")
birthYear = input("Enter birth year: ")
birthYear = int(birthYear)
age = currentYear - birthYear

dictionary = {
        'first_name' : firstName,
        'second_name' : secondName,
        'third_name' : thirdName,
        'current_age' : age
    }

print(dictionary)
