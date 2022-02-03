def f() -> int:
    print("start f")
    g()
    $Statement
    return 42

    
def g() -> object:
    print("start g")
    h()
    print("end g")

def h() -> object:
    print("start h")
    print("end h")

print(f())
