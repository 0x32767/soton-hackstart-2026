from soton_hackstart_2026.interpreter import Interpreter, Direction
from soton_hackstart_2026.parser import Parser
from soton_hackstart_2026.stack import Stack


def run(text: str, input_func, output_func):
    parser = Parser(text)

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

    alive = True
    while alive:
        for interpreter in interpreters:
            alive = alive or (not interpreter.terminated)
            interpreter.advance(parser, memory, parser.size, input_func=input_func, output_func=output_func)

def main() -> None:
    import soton_hackstart_2026.IDE_GUI
