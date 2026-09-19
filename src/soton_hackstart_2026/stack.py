class Stack:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.px = 0
        self.py = 0
        self.data = {}

    def pointer_up(self):

        self.py -= 1
        assert 0 <= self.py <= self.width, f"{self.py} {self.width}"

    def pointer_down(self):
        self.py += 1
        assert 0 <= self.py <= self.width, f"{self.py} {self.width}"

    def pointer_left(self):
        self.px -= 1
        assert 0 <= self.px <= self.width, f"{self.px} {self.width}"

    def pointer_right(self):
        self.px += 1
        assert 0 <= self.px <= self.width, f"{self.px} {self.width}"

    def increment(self):
        self.data[(self.px, self.py)] = (self.data.get((self.px, self.py), 0) + 1) % 256

    def decrement(self):
        self.data[(self.px, self.py)] = (self.data.get((self.px, self.py), 0) - 1) % 256

    def read(self):
        return chr(self.data[(self.px, self.py)])

    def read_raw(self):
        return self.data.get((self.px, self.py), 0)

    def write(self, value: int):
        self.data[(self.px, self.py)] = value
