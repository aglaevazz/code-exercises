# this program creates a trie of patterns and gets the starting positions of those patterns in a given text


class Node:
    def __init__(self, index, letter=None):
        self.index = index
        self.letter = letter
        self.next = {}
        self.end_of_pattern = False


class PatternTrie:
    def __init__(self, n):
        self.n = n
        self.root = Node(0, 'root')
        self.clock = 1
        self.adjacency_list = [self.root]
        self.safe_trie()

    def safe_trie(self):
        for _ in range(n):
            pattern = input()
            current = self.root
            for index in range(len(pattern)):
                letter = pattern[index]
                if letter in current.next:
                    if index == len(pattern) - 1:
                        current.next[letter].end_of_pattern = True
                    current = current.next[letter]
                elif letter not in current.next:
                    self.add_pattern(current, pattern[index:])
                    break

    def add_pattern(self, node, pattern):
        current = node
        for i in range(len(pattern)):
            letter = pattern[i]
            new_node = Node(self.clock, letter)
            if i == len(pattern) - 1:
                new_node.end_of_pattern = True
            current.next[letter] = new_node
            self.clock += 1
            current = new_node
            self.adjacency_list.append(new_node)

    def print_trie(self):
        for node in self.adjacency_list:
            for next_node in node.next.values():
                print(str(node.index)+'->'+str(next_node.index)+':'+next_node.letter)

    def get_starting_positions_patterns(self, text):
        starting_positions = []
        index = 0
        for _ in text:
            current_index = index
            current_letter = text[current_index]
            current_node = self.root
            while current_index <= len(text):
                if not current_node.next or current_node.end_of_pattern == True:
                    starting_positions.append(index)
                    break
                elif current_letter in current_node.next:
                    current_index += 1
                    current_node = current_node.next[current_letter]
                    if current_index < len(text):
                        current_letter = text[current_index]
                else:
                    break
            index += 1
        return starting_positions


if __name__ == '__main__':
    text = input()
    n = int(input())
    trie = PatternTrie(n)
    print(' '.join(str(element) for element in trie.get_starting_positions_patterns(text)))