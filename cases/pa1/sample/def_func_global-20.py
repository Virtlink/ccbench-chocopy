z:int = 0

def foo(x:int) -> $ID:
    global z
    return x > z

foo(1)
