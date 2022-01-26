def outer() -> int:
    def inner() -> int:
        nonlocal x
        x = [[Exp]]
        return x
    x:int = 0
    inner()
    return x

print(outer())
