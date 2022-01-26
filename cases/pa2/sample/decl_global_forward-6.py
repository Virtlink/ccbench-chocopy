def set_x() [[RetType]]:
    global x
    x = 1
    return x

x:int = 0

set_x()
print(x)
