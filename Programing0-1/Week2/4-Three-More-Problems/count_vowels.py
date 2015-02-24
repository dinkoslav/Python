word = input("Enter word: ")

vowels = "aeiouyAEIOUY"
count = 0

for ch in word:
    if ch in vowels:
        count = count + 1

print(count)
