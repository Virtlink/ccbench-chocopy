class A(object):
    a:int = 42

class B(A):
    $ClassBodyMember

    def __init__(self:"B"):
        print("B")


B()
