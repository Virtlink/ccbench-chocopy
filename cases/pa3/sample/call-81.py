def f() -> int:
    print("start f")
    g()
    print("end f")
    return 42

    
def g() -> object:
    print("start g")
    h()
    print("end g")

[[FuncDef]]

print(f())
