word = input("Enter word: ")
n = input("Enter n: ")
n = int(n)

count = 1
total = 0

while count <= n:
    input_word = input()
    if word in input_word:
        total = total + 1
    count = count + 1

print(word + " is found " + str(total) + " times.")
