def count_vowels_consonants(word):
    dict = {
            "vowels" : 0,
            "consonants" : 0
        }
    vovels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    count = 0
    
    while count < len(word):
        if word[count] in vovels:
            dict["vowels"] = dict["vowels"] + 1
        else:
            dict["consonants"] = dict["consonants"] + 1
        count = count + 1

    return dict

test = count_vowels_consonants("aaaAcccD")
print(test)
