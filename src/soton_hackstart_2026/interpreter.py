from enum import StrEnum, auto


class Direction(StrEnum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()

class Interpreter:
    def __init__(self, start_x: int, start_y: int, direction: Direction):
        self.direction = direction
        self.x = start_x
        self.y = start_y
        self.terminated = False
        self.ignore = False

    def advance(self, parser, memory, width, input_func, output_func):
        print("Int:", self.x, self.y, self.direction)
        print("MEM:", memory.data)
        if self.terminated:
            return

        if self.direction == Direction.RIGHT:
            self.x += 1
        elif self.direction == Direction.LEFT:
            self.x -= 1
        elif self.direction == Direction.UP:
            self.y -= 1
        elif self.direction == Direction.DOWN:
            self.y += 1

        assert 0 <= self.x <= width, f"fell off to the left or right {self.x} between 0 and {width}"
        assert 0 <= self.y <= width, f"Fell off to the top or bottom {self.y} between 0 and {width}"

        if self.ignore:
            self.ignore = False
            return

        instruction = parser.read_instruction(self.x, self.y)

        if instruction == "+":
            memory.increment()
        elif instruction == "-":
            memory.decrement()
        elif instruction == "<":
            memory.pointer_left()
        elif instruction == ">":
            memory.pointer_right()
        elif instruction == "^":
            memory.pointer_up()
        elif instruction == "v":
            memory.pointer_down()
        elif instruction == "i":
            data = input_func()
            if len(data) == 1:
                memory.write(ord(data))
            elif len(data) == 0:
                memory.write(0)
            else:
                assert False
        elif instruction == "o":
            char = memory.read()
            output_func(char)
        elif instruction == " ":
            return
        elif instruction == "/":
            self.direction = {
                Direction.LEFT: Direction.DOWN,
                Direction.RIGHT: Direction.UP,
                Direction.UP: Direction.RIGHT,
                Direction.DOWN: Direction.LEFT,
            }[self.direction]
        elif instruction == "\\":
            self.direction = {
                Direction.LEFT: Direction.UP,
                Direction.RIGHT: Direction.DOWN,
                Direction.DOWN: Direction.RIGHT,
                Direction.UP: Direction.LEFT,
            }[self.direction]
        elif instruction == "|":
            self.direction = {
                Direction.LEFT: Direction.RIGHT,
                Direction.RIGHT: Direction.LEFT
            }[self.direction]
        elif instruction == "_":
            self.direction = {
                Direction.UP: Direction.DOWN,
                Direction.DOWN: Direction.UP
            }[self.direction]
        elif instruction == "t":
            self.terminated = True
        elif instruction == "x":
            self.ignore = (memory.read_raw() == 0)
            print(self.ignore)
        elif instruction == "X":
            self.ignore = (memory.read_raw() != 0)
        elif instruction in "lrud":
            return
        else:
            raise NotImplementedError(istruction)

        print("Mem:", memory.px, memory.py, memory.read_raw())
