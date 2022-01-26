z:int = 0

def foo(x:int) [[RetType]]:
    global z
    return x > z

foo(1)
