def outer() -> int:
    def inner() -> int:
        
        x = 1
        return x
    x:int = 0
    inner()
    return x

print(outer())
