def outer() -> int:
    def inner() -> int:
        [[FuncBody]]
    x:int = 0
    inner()
    return x

print(outer())
