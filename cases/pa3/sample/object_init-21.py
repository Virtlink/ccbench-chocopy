class A(object):
    a:int = 42

class B(A):
    $TypedVar = True

    def __init__(self:"B"):
        print("B")


B()
