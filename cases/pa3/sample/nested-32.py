g: int = 1
def foo(x: int) -> int:
    y: int = 2
    $FuncDef
    return bar()
    
print(foo(g))
