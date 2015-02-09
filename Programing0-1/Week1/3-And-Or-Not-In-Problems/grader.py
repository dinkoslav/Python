points = input("Enter a number between 0 and 100: ")
points = int(points)

if points < 0 or 100 < points:
    print("Invalid number!")
elif 0 < points <= 50:
    print("Слаб 2")
elif 51 <= points <= 60:
    print("Среден 3")
elif 61 <= points <= 70:
    print("Добър 4")
elif 71 <= points <= 80:
    print("Много Добър 5")
elif 81 <= points <= 90:
    print("Отличен 6")
elif 91 <= points <= 100:
    print("Много Отличен 7")
