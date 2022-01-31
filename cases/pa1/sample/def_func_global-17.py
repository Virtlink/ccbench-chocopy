z:int = 0

def foo(x:$ID) -> bool:
    global z
    return x > z

foo(1)
