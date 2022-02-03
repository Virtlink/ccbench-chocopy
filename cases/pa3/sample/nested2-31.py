g: int = 1
def foo(x: int) -> int:
    y: int = 2
    $FuncBodyMember
    def qux(p: int) -> int:
        return p

    return bar()
    
print(foo(g))
