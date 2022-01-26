def foo(x:str, y:bool) -> int:
    return bar()

def bar() [[RetType]]:
    return 1

foo("Hello", False)
