def outer() -> int:
    def inner() -> int:
        nonlocal x
        x = 1
        return x
    $VarDef
    inner()
    return x

print(outer())
