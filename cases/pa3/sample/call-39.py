def f() -> int:
    print("start f")
    g()
    print("end f")
    return 42

    
def g() $RetType:
    print("start g")
    h()
    print("end g")

def h() -> object:
    print("start h")
    print("end h")

print(f())
