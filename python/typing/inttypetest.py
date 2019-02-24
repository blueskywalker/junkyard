from typing import Any

def echo_int(data: int) -> None:
    print(data)

def echo(data: Any) -> None:
    print(data)

input_data = [ 10, 'a', 2, [ 2, "b"] ]

for item in input_data:
    echo_int(item)
    echo(item)
