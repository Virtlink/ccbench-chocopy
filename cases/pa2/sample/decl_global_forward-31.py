def set_x() -> int:
    global x
    x = 1
    return x

x:$Type = 0

set_x()
print(x)
