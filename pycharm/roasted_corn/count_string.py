def count_string(words):
    new_word = []
    for word in words:
        if len(word) > 2:
            if word[0] == word[-1]:
                new_word.append(word)
    return new_word

word = ["oyo", "mallam" , "qw", "level"]
print(count_string(word))
