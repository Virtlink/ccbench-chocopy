def set_x() -> int:
    global x
    x = $Literal
    return x

x:int = 0

set_x()
print(x)
