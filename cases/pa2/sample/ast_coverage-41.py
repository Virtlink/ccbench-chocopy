count:int = 0

def foo(s: str) -> int:
    return len(s)

class bar(object):
    p: bool = True

    $ClassBodyMember

print(bar().baz([1,2]))


