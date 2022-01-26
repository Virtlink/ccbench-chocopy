count:int = 0

def foo(s: str) -> int:
    return len(s)

class bar(object):
    p: bool = True

    def baz(self:"bar", xx: [int]) -> str:
        global count
        x:int = 0
        y:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        

print(bar().baz([1,2]))


