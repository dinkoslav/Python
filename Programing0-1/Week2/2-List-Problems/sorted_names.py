n = input("Enter n: ")
n = int(n)

count = 1
names = []

while count <= n:
    input_word = input()
    names = names + [input_word]
    count = count + 1

names = sorted(names)
for name in names:
    print(name)
