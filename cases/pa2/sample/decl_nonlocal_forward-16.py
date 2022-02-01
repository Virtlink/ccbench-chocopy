def outer() -> int:
    def inner() -> int:
        nonlocal $ID
        x = 1
        return x
    x:int = 0
    inner()
    return x

print(outer())
