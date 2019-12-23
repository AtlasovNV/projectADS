def title_slice(keywords_split):
    first_title = []
    second_title = []
    counter = -1
    keywords_split = keywords_split.split()
    for word in keywords_split:
        counter += len(word) + 1
        if counter <= 35:
            first_title.append(word)
        else:
            second_title.append(word)
    first_title = ' '.join(word for word in first_title)
    second_title = ' '.join(word for word in second_title)
    if second_title is not '':
        new_list = [first_title, second_title]
    else:
        new_list = [first_title, '-']
    return new_list
