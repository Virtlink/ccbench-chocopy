def set_x() -> int:
    global x
    [[Target]] = 1
    return x

x:int = 0

set_x()
print(x)
