g: int = 1
def foo(x: int) -> int:
    [[VarDef]]
    def bar() -> int:
        z: int = 3
        def baz() -> int:
            return y
        return baz()
    return bar()
    
print(foo(g))
