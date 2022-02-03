def f(x:int) -> int:
    print("start f")
    print(x)
    g(1, x)
    print("end f")
    return x

    
def g(y:int, z:int) -> object:
    print("start g")
    print(y)
    print(z)
    h("h")
    print($Literal)

def h(msg: str) -> object:
    print(msg)

print(f(4))
