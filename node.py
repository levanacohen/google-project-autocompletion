class Node:
    def __init__(self, letter, parent, source):
        self.letter = letter
        self.sons = {}
        self.parent = parent
        self.height = -1
        self.sources = {(source.path, source.line):source.offset}

    def add_son(self, letter, source):
        if self.sons.get(letter):
            key_source = (source.path, source.line)
            if not key_source in self.sons[letter].sources:
                self.sons[letter].sources[key_source] = source.offset
        else:
            self.sons[letter] = Node(letter, self, source)
        return self.sons[letter]
