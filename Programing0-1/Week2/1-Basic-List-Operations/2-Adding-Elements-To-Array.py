languages = ["Python", "Ruby"]
languages = languages + ["C++", "Java", "C#"]
languages = ["Haskel"] + languages
languages = languages + ["Go"]
print(languages)

print(languages[0])
print(languages[1])
print(languages[4])

index = 0
while index < len(languages)-1:
    if "C#" in languages[index]:
        languages[index] = "F#"
    index = index + 1

print(languages)
print(languages[len(languages)-1])

print("Haskell" in languages)
print("Ruby" in languages)
print("Go" in languages)
print("Rust" in languages)
