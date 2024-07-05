def single_root_words (root_word,*other_words):
    same_words = list()
    for i in range(len(other_words)):
        if root_word in other_words[i]:
            same_words.append(other_words[i])
    return same_words
example1 = 'кор'
example2 ='ен'
rezult1 = single_root_words(example1,'корень','комментатора','корешок','очень','флейтешок','преувеличен')
rezult2 = single_root_words(example2,'корень','комментатора','корешок','очень','флейтешок','преувеличен')
print (f'Для "{example1}" совпадения:{rezult1}')
print (f'Для "{example2}" совпадения:{rezult2}')