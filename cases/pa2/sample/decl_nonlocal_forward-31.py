def outer() -> int:
    def inner() -> int:
        nonlocal x
        x = [[INT]]
        return x
    x:int = 0
    inner()
    return x

print(outer())
