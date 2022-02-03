def outer() -> int:
    def inner() -> int:
        nonlocal x
        x = 1
        return x
    x:int = $INT
    inner()
    return x

print(outer())
