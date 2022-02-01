def foo(x:str, y:$Type) -> int:
    return bar()

def bar() -> int:
    return 1

foo("Hello", False)
