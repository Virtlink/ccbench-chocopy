
def foo(x:int) -> bool:
    a:int = 0
    b:int = 1
    def bar(y: int) -> int:
        nonlocal a
        a = 2 
        return y
    return $Var(x) > a

foo(1)
