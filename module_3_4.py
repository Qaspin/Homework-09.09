def single_root_words(root_word, *other_words):
    same_words = []
    words = list(other_words)

    for j in range(len(words)):
        if root_word.upper() in words[j] or words[j].upper() in root_word.upper():
            same_words.append(words[j])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
