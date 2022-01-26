class A(object):
    a:int = 42

class B(A):
    b:bool = True

    def __init__(self:"B"):
        print("B")

a:A = None
b:B = None

def get_b() -> B:
    print("Getting B")
    return b

def get_one() -> int:
    print("Getting 1")
    return 1

def get_false() -> bool:
    print("Getting False")
    return False


