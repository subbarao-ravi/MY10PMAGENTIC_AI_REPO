from collections.abc import Callable

def apply(func : Callable[[int, int], int], a:int, b: int) -> int:
    return func(a, b)


def add(a,b):
    return a+b


print(apply(add, 2 , 3))