def decode_word(encrypted_word, cipher):
    word = ""
    for e in range(0, len(encrypted_word)):
        element = encrypted_word[e]
        crypthed_letter = find_proper_key(element, cipher)
        word += crypthed_letter

    return word

def find_proper_key(letter, cipher):
    for key in cipher:
        if cipher[key] == letter:
            return key

print(decode_word("mjriew", {'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'}))
print(decode_word("rpf", {'m': 'p', 'o': 'r', 'g': 'f'}))
print(decode_word("wfhsftzzuys", {'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'}))
print(decode_word("bbbbbbbbbbbbbbbbbbbbbbbbbbb", {'a': 'b'}))
