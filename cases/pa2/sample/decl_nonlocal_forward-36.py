def outer() -> int:
    def inner() -> int:
        nonlocal x
        x = 1
        return x
    [[FuncBodyMember]]
    inner()
    return x

print(outer())
