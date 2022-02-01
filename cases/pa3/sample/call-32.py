def f() -> int:
    print("start f")
    g()
    print("end f")
    $Statement

    
def g() -> object:
    print("start g")
    h()
    print("end g")

def h() -> object:
    print("start h")
    print("end h")

print(f())
