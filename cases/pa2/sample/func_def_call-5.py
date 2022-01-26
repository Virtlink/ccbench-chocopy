def foo() -> int:
    return bar()

def bar() -> int:
    return 1

foo("Hello", False)
