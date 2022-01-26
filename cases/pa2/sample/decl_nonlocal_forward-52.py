def outer() -> int:
    def inner() -> int:
        nonlocal x
        x = 1
        return x
    x:int = 0
    inner()
    [[Statement]]

print(outer())
