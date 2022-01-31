class A(object):
    a:int = 42

class B(A):
    b:bool = $Literal

    def __init__(self:"B"):
        print("B")


B()
