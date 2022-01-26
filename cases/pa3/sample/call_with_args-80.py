def f(x:int) -> int:
    print("start f")
    print(x)
    g(1, x)
    print("end f")
    return x

    
def g(y:int, z:int) -> object:
    

def h(msg: str) -> object:
    print(msg)

print(f(4))
