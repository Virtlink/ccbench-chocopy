def set_x() -> int:
    global x
    x = 1
    return x

x:int = $Literal

set_x()
print(x)
