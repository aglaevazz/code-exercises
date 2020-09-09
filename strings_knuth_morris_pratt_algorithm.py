# python 3
# here I implemented the knuth-morris-pratt algorithm to find the indices of occurrences of a pattern in a text (genome)


def get_indices_where_pattern_starts_in_text(pattern, text):
    if len(pattern) <= len(text):
        indices_where_pattern_starts = []
        knuth_morris_pratt_string = pattern + '§' + text
        borders_of_prefixes = prefix_function(knuth_morris_pratt_string)
        for i in range(len(pattern) + 1, len(knuth_morris_pratt_string)):
            if borders_of_prefixes[i] == len(pattern):
                indices_where_pattern_starts.append(i-len(pattern)*2)
        return indices_where_pattern_starts


def prefix_function(string):
    borders_of_prefixes = [0 for _ in range(len(string))]
    border = 0
    for i in range(1, len(string)):
        while border > 0 and string[i] != string[border]:
            border = borders_of_prefixes[border - 1]
        if string[i] == string[border]:
            border += 1
        else:
            border = 0
        borders_of_prefixes[i] = border
    return borders_of_prefixes


if __name__ == '__main__':
    pattern = input()
    text = input()
    indices = get_indices_where_pattern_starts_in_text(pattern, text)
    if indices:
        print(' '.join(str(i) for i in indices))
