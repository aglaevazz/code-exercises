# this program constructs the wheeler_burrow_transform from a given text


def get_burrow_wheeler_transform(text):
    burrow_wheeler_matrix = [text]
    current_text = text
    for _ in range(len(text)-1):
        new_text = current_text[-1]+current_text[:-1]
        burrow_wheeler_matrix.append(new_text)
        current_text = new_text
    burrow_wheeler_matrix.sort()
    burrow_wheeler_transform = ''
    for string in burrow_wheeler_matrix:
        burrow_wheeler_transform += string[-1]
    return burrow_wheeler_transform


if __name__ == '__main__':
    text = input()
    print(get_burrow_wheeler_transform(text))
