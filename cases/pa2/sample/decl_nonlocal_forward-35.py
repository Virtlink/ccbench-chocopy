def outer() -> int:
    def inner() -> int:
        nonlocal x
        x = 1
        return x
    x:int = $Literal
    inner()
    return x

print(outer())
