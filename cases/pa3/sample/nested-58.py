g: int = 1
def foo(x: int) -> int:
    y: int = 2
    def bar() -> int:
        z: int = 3
        def baz() -> int:
            $Statement
        return baz()
    return bar()
    
print(foo(g))
