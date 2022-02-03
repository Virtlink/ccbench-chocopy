
def foo(x:int) -> bool:
    a:$Type = 0
    b:int = 1
    def bar(y: int) -> int:
        a:int = 2 
        return y
    return bar(x) > a

foo(1)
