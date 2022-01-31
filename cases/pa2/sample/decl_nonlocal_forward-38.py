def outer() -> int:
    def inner() -> int:
        nonlocal x
        x = 1
        return x
    $TypedVar = 0
    inner()
    return x

print(outer())
