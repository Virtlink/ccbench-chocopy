def f() -> int:
    print("start f")
    g()
    print("end f")
    return 42

    
def g() -> object:
    print("start g")
    $Var()
    print("end g")

def h() -> object:
    print("start h")
    print("end h")

print(f())
