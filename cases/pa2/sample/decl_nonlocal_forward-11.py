def outer() -> int:
    [[FuncBodyMember]]
    x:int = 0
    inner()
    return x

print(outer())
