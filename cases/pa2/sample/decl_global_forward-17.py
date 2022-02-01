def set_x() -> int:
    global x
    x = $INT
    return x

x:int = 0

set_x()
print(x)
