class A(object):
    a:int = $Literal

class B(A):
    b:bool = True

    def __init__(self:"B"):
        print("B")


B()
