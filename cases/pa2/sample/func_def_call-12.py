def foo(x:str, y:bool) $RetType:
    return bar()

def bar() -> int:
    return 1

foo("Hello", False)
