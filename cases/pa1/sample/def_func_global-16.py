z:int = 0

def foo(x:[[Type]]) -> bool:
    global z
    return x > z

foo(1)
