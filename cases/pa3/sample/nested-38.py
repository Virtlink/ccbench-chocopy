g: int = 1
def foo(x: int) -> int:
    y: int = 2
    def bar() -> int:
        $FuncBody
    return bar()
    
print(foo(g))
