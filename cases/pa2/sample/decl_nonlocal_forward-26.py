def outer() -> int:
    def inner() -> int:
        nonlocal x
        x = 1
        return $Exp
    x:int = 0
    inner()
    return x

print(outer())
