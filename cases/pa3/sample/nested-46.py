g: int = 1
def foo(x: int) -> int:
    y: int = 2
    def bar() -> int:
        z: int = [[Literal]]
        def baz() -> int:
            return y
        return baz()
    return bar()
    
print(foo(g))
