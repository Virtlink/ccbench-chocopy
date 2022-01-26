count:int = 0

def foo(s: str) -> int:
    return len(s)

class bar(object):
    p: bool = True

    def baz(self:"bar", xx: [int]) -> str:
        [[FuncBody]]

print(bar().baz([1,2]))


