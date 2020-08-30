# this program reconstructs the original text from the burrow_wheeler_transform


def get_text_from_burrow_wheeler_transform(burrows_wheeler_transform):
    dict_fist_last_column = store_as_dict(sorted(burrows_wheeler_transform), burrows_wheeler_transform)
    text = ['$1']
    while len(text) < len(burrows_wheeler_transform):
        previous_letter = dict_fist_last_column[text[-1]]
        text.append(previous_letter)
    text.reverse()
    return ''.join(i[0] for i in text)


def store_as_dict(first_column, last_column):
    indices_first_column = {'A': 1, 'G': 1, 'T': 1, 'C': 1, '$': 1}
    indices_last_column = {'A': 1, 'G': 1, 'T': 1, 'C': 1, '$': 1}
    dict_fist_last_column = {}
    for letter_first_column, letter_last_column in zip(first_column, last_column):
        dict_fist_last_column[letter_first_column+str(indices_first_column[letter_first_column])] = \
            letter_last_column + str(indices_last_column[letter_last_column])
        indices_first_column[letter_first_column] += 1
        indices_last_column[letter_last_column] += 1
    return dict_fist_last_column


if __name__ == '__main__':
    burrow_wheeler_transform = input()
    print(get_text_from_burrow_wheeler_transform(burrow_wheeler_transform))
