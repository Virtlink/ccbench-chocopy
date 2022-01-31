def f(x:int) -> int:
    $FuncBody

    
def g(y:int, z:int) -> object:
    print("start g")
    print(y)
    print(z)
    h("h")
    print("end g")

def h(msg: str) -> object:
    print(msg)

print(f(4))
