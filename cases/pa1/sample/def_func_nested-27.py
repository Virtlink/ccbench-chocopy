
def foo(x:int) -> bool:
    a:int = 0
    b:int = $INT
    def bar(y: int) -> int:
        a:int = 2 
        return y
    return bar(x) > a

foo(1)
