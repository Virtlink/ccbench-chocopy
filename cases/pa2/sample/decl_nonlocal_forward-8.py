def outer() -> [[ID]]:
    def inner() -> int:
        nonlocal x
        x = 1
        return x
    x:int = 0
    inner()
    return x

print(outer())