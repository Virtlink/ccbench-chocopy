def outer() -> int:
    $FuncDef
    x:int = 0
    inner()
    return x

print(outer())
