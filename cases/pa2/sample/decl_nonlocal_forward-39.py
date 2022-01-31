def outer() -> int:
    def inner() -> int:
        nonlocal x
        x = 1
        return x
    $ID:int = 0
    inner()
    return x

print(outer())
