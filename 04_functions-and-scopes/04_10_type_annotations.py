# Add type annotations to the three functions shown below.
# type annotations are also known as type signatures and they are used to indicate the data type of variables and the input
# and output of functions and methods in a programming language
# static type: performs type checking at compile-time and requires datattype declarations
# dynamic type: performs type checking at runtime and does not require datatype declarations


def multiply(num1: int, num2: int):
    return num1 * num2


def greet(greeting: str, name: str):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence


def shopping_list(*args: str):
    [print(f"* {item}") for item in args]
    return args
