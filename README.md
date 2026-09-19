# Bramble
2d esolang with 2d memory matrix of the same size as the program

## Interpreter management
The descriptions are formatted as [read direction A:read direction B], and if the interpreter is reading from either direction it will read in the new direction instead.
If a direction is not mentioned, an error will be raised
|Opcode|Description|
|---|---|
|t|Terminate program (note: The bramble interpreter will throw an error if it reaches the edge of the square before hitting this opcode)|
|u|Start thread in this position heading up when the program is run|
|d|Start thread in this position heading down when the program is run|
|l|Start thread in this position heading left when the program is run|
|r|Start thread in this position heading right when the program is run|
|/|[left:up][right:down]|
| \\ |[left:down][right:up]|
|\||[left:left][right:right]|
|-|[up:up][down:down]|
|x|If the current memory cell is 0, the next opcode hit is ignored|

## Memory management
|Opcode|Description|
|------|-----------|
|+|Increment the top of the current stack|
|-|Decrement top of current stack|
|<|Move pointer left|
|>|Move pointer right|
|^|Move pointer up|
|v|Move pointer down|
|i|Waits for ascii keypress and writes value to the current cell of the memory matrix|
|o|Outputs the value of the current cell as an ascii character|
