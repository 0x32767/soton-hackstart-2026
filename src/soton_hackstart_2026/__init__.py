from soton_hackstart_2026.interpreter import Interpreter, Direction
from soton_hackstart_2026.parser import Parser
from soton_hackstart_2026.stack import Stack


def run():
    with open("examples/cat.brm", "r") as f:
        parser = Parser(f.read())

    memory = Stack(parser.size, parser.size)
    interpreters = [
        Interpreter(
            x,
            y,
            {
                "l": Direction.LEFT,
                "r": Direction.RIGHT,
                "u": Direction.UP,
                "d": Direction.DOWN
            }[direction]
        )
        for (x, y), direction in parser.get_starts()
    ]

    while True:
        for interpreter in interpreters:
            interpreter.advance(parser, memory, parser.size)

def main() -> None:
    run()
