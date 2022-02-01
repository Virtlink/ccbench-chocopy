g: int = 1
def foo(x: int) -> int:
    y: int = $Literal
    def bar() -> int:
        z: int = 3
        def baz() -> int:
            return qux(y)
        return baz()
    def qux(p: int) -> int:
        return p

    return bar()
    
print(foo(g))
