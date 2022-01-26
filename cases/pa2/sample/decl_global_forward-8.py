def set_x() -> [[ID]]:
    global x
    x = 1
    return x

x:int = 0

set_x()
print(x)
