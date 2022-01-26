def set_x() -> int:
    global x
    x = 1
    return x

[[TypedVar]] = 0

set_x()
print(x)
