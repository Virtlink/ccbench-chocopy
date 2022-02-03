def outer() -> int:
    def inner() -> int:
        nonlocal x
        x = 1
        $Statement
    x:int = 0
    inner()
    return x

print(outer())
