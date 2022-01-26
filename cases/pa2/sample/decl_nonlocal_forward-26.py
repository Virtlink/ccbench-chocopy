def outer() -> int:
    def inner() -> int:
        nonlocal x
        [[Target]] = 1
        return x
    x:int = 0
    inner()
    return x

print(outer())
