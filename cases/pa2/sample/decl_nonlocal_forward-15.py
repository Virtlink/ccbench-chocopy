def outer() -> int:
    def inner() [[RetType]]:
        nonlocal x
        x = 1
        return x
    x:int = 0
    inner()
    return x

print(outer())
