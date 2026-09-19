class Parser:
    def __init__(self, code):
        self.code = {}

        line_number = 0
        for line_number, line in enumerate(code.splitlines()):
            for char_number, char in enumerate(line):
                self.code[(char_number, line_number)] = char

        self.size = line_number

    def read_instruction(self, x, y):
        try:
            return self.code[(x, y)]
        except Exception:
            return " "

    def get_starts(self):
        for (x, y), instruction in self.code.items():
            if instruction in "lrud":
                yield (x, y), instruction
