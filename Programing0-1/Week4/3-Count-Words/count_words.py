def count_words(words):
    dict = {}
    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] = dict[word] + 1
            
    return dict

words = ["words", "are", "meaningful", "words", "words", "are"]

dictionary = count_words(words)
print(dictionary)
