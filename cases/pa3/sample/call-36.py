def f() -> int:
    print("start f")
    g()
    print("end f")
    return 42

    
$Definition

def h() -> object:
    print("start h")
    print("end h")

print(f())
