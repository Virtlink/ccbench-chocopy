def outer() -> int:
    def inner() -> $ID:
        nonlocal x
        x = 1
        return x
    x:int = 0
    inner()
    return x

print(outer())
