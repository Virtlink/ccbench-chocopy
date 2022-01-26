g: int = 1
def foo(x: int) -> int:
    y: int = 2
    [[FuncBodyMember]]
    return bar()
    
print(foo(g))
