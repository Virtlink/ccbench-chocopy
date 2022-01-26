g: int = 1
def [[ID]](x: int) -> int:
    y: int = 2
    def bar() -> int:
        z: int = 3
        def baz() -> int:
            return y
        return baz()
    return bar()
    
print(foo(g))
