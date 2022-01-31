z:int = 0

def foo(x:int) -> bool:
    global z
    return x > $Var

foo(1)
