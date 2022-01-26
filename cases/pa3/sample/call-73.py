def f() -> int:
    print("start f")
    g()
    print("end f")
    return 42

    
def g() -> object:
    print("start g")
    h()
    [[Var]]("end g")

def h() -> object:
    print("start h")
    print("end h")

print(f())
