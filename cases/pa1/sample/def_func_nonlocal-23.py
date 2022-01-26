
def foo(x:int) -> bool:
    a:int = 0
    [[FuncBodyMember]]
    def bar(y: int) -> int:
        nonlocal a
        a = 2 
        return y
    return bar(x) > a

foo(1)
