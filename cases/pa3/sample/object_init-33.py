class A(object):
    a:int = 42

class B(A):
    b:bool = True

    def __init__([[TypedVar]]):
        print("B")


B()
