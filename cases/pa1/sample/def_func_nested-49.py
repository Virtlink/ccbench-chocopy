
def foo(x:int) -> bool:
    a:int = 0
    b:int = 1
    def bar(y: int) -> int:
        a:$ID = 2 
        return y
    return bar(x) > a

foo(1)
