z:int = 0

def foo() -> bool:
    global z
    return x > z

foo(1)
