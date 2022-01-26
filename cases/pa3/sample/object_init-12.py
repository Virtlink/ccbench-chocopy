class A(object):
    a:[[Type]] = 42

class B(A):
    b:bool = True

    def __init__(self:"B"):
        print("B")


B()
