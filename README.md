# ASDFGHJKL
2d esolang with 2d memory tape of the same size as your program


## Pointer management
|Opcode|Description|
|------|-----------|
|kys|Terminate program (note: ASDFGHJKL interpreter will throw an error if it reaches the edge of the square before hitting this opcode)|
|+|Increment the top of the current stack|
|-|Decrement top of current stack|
|<|Move pointer left|
|>|Move pointer right|
|^|Move pointer up|
|v|Move pointer down|

## Interpreter management
The descriptions are formatted as [read direction A:read direction B], and if the interpreter is reading from either direction it will read in the new direction instead.
If a direction is not mentioned, an error will be raised
|Opcode|Description|
|---|---|
|/|[left:up][right:down]|
|\\|[left:down][right:up]|
|\||[left:left][right:right]|
|-|[up:up][down:down]|
