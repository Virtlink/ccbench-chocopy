def foo(x:str, $TypedVar) -> int:
    return bar()

def bar() -> int:
    return 1

foo("Hello", False)
