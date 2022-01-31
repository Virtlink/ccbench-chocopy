def foo(x:str, y:$ID) -> int:
    return bar()

def bar() -> int:
    return 1

foo("Hello", False)
