def single_root_words (root_word,*other_words):
    same_words = list()
    upper_root_word = root_word.upper()
    upper_other_words = list()
    for j in range(len(other_words)):
        x = other_words[j].upper()
        upper_other_words.append(x)
    for i in range(len(upper_other_words)):
        if upper_root_word in upper_other_words[i] or upper_other_words[i] in upper_root_word:
            same_words.append(other_words[i])
    return same_words
example1 = 'Интер'
example2 ='Инь'
rezult1 = single_root_words(example1,'ин','интернеТ','интернационал','очень','инт','курятина')
rezult1.insert(0,example1)
rezult2 = single_root_words(example2,'ин','интернеТ','интернационал','очень','инт','курятина')
rezult2.insert(0,example2)
print (f'Для "{example1}" совпадения:{rezult1}')
print (f'Для "{example2}" совпадения:{rezult2}')