
def foo(x:int) $RetType:
    a:int = 0
    b:int = 1
    def bar(y: int) -> int:
        a:int = 2 
        return y
    return bar(x) > a

foo(1)
