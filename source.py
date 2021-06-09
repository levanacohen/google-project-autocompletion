class Source:
    def __init__(self, path, line, offset):
        self.path = path
        self.line = line
        self.offset = offset

    def copy_inc_offset(self, offset):
        s = Source(self.path, self.line, self.offset + offset)
        return s

    def copy_inc_line(self, l):
        s = Source(self.path, self.line + l, self.offset)
        return s