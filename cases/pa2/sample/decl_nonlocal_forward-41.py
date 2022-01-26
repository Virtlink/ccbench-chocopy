def outer() -> int:
    def inner() -> int:
        nonlocal x
        x = 1
        return x
    x:[[ID]] = 0
    inner()
    return x

print(outer())
