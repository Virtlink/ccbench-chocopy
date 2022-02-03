count:int = 0
count2:int = 0
count3:int = 0
count4:int = 0
count5:int = 0

def foo(s: str) -> int:
    return len(s)

def foo2(s: str, s2: str) -> int:
    return len(s)

def foo3(s: str, s2: str, s3: str) -> int:
    return len(s)

def foo4(s: str, s2: str, s3: str, s4: str) -> int:
    return len(s)

def foo5(s: str, s2: str, s3: str, s4: str, s5: str) -> int:
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

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"


class bar2(object):
    p: bool = True
    p2: bool = True

    def baz(self:"bar2", xx: [int]) -> str:
        global count
        x:int = 0
        y:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"


    def baz2(self:"bar2", xx: [int], xx2: [int]) -> str:
        global count
        x:int = 0
        x2:int = 0
        y:int = 1
        y2:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        def qux2(y: int, y2: int) -> object:
            nonlocal x
            nonlocal x2
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"



class bar3(object):
    p: bool = True
    p2: bool = True
    p3: bool = True

    def baz(self:"bar3", xx: [int]) -> str:
        global count
        x:int = 0
        y:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"


    def baz2(self:"bar3", xx: [int], xx2: [int]) -> str:
        global count
        x:int = 0
        x2:int = 0
        y:int = 1
        y2:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        def qux2(y: int, y2: int) -> object:
            nonlocal x
            nonlocal x2
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"

    def baz3(self:"bar3", xx: [int], xx2: [int], xx3: [int]) -> str:
        global count
        x:int = 0
        x2:int = 0
        x3:int = 0
        y:int = 1
        y2:int = 1
        y3:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        def qux2(y: int, y2: int) -> object:
            nonlocal x
            nonlocal x2
            if x > y:
                x = -1

        def qux3(y: int, y2: int, y3: int) -> object:
            nonlocal x
            nonlocal x2
            nonlocal x3
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"



class bar4(object):
    p: bool = True
    p2: bool = True
    p3: bool = True
    p4: bool = True

    def baz(self:"bar4", xx: [int]) -> str:
        global count
        x:int = 0
        y:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"


    def baz2(self:"bar4", xx: [int], xx2: [int]) -> str:
        global count
        x:int = 0
        x2:int = 0
        y:int = 1
        y2:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        def qux2(y: int, y2: int) -> object:
            nonlocal x
            nonlocal x2
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"

    def baz3(self:"bar4", xx: [int], xx2: [int], xx3: [int]) -> str:
        global count
        x:int = 0
        x2:int = 0
        x3:int = 0
        y:int = 1
        y2:int = 1
        y3:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        def qux2(y: int, y2: int) -> object:
            nonlocal x
            nonlocal x2
            if x > y:
                x = -1

        def qux3(y: int, y2: int, y3: int) -> object:
            nonlocal x
            nonlocal x2
            nonlocal x3
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"

    def baz4(self:"bar4", xx: [int], xx2: [int], xx3: [int], xx4: [int]) -> str:
        global count
        x:int = 0
        x2:int = 0
        x3:int = 0
        x4:int = 0
        y:int = 1
        y2:int = 1
        y3:int = 1
        y4:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        def qux2(y: int, y2: int) -> object:
            nonlocal x
            nonlocal x2
            if x > y:
                x = -1

        def qux3(y: int, y2: int, y3: int) -> object:
            nonlocal x
            nonlocal x2
            nonlocal x3
            if x > y:
                x = -1

        def qux4(y: int, y2: int, y3: int, y4: int) -> object:
            nonlocal x
            nonlocal x2
            nonlocal x3
            nonlocal x4
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"


class bar5(object):
    p: bool = True
    p2: bool = True
    p3: bool = True
    p4: bool = True
    p5: bool = True

    def baz(self:"bar5", xx: [int]) -> str:
        global count
        x:int = 0
        y:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"


    def baz2(self:"bar5", xx: [int], xx2: [int]) -> str:
        global count
        x:int = 0
        x2:int = 0
        y:int = 1
        y2:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        def qux2(y: int, y2: int) -> object:
            nonlocal x
            nonlocal x2
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"

    def baz3(self:"bar5", xx: [int], xx2: [int], xx3: [int]) -> str:
        global count
        x:int = 0
        x2:int = 0
        x3:int = 0
        y:int = 1
        y2:int = 1
        y3:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        def qux2(y: int, y2: int) -> object:
            nonlocal x
            nonlocal x2
            if x > y:
                x = -1

        def qux3(y: int, y2: int, y3: int) -> object:
            nonlocal x
            nonlocal x2
            nonlocal x3
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return $STRING

    def baz4(self:"bar5", xx: [int], xx2: [int], xx3: [int], xx4: [int]) -> str:
        global count
        x:int = 0
        x2:int = 0
        x3:int = 0
        x4:int = 0
        y:int = 1
        y2:int = 1
        y3:int = 1
        y4:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        def qux2(y: int, y2: int) -> object:
            nonlocal x
            nonlocal x2
            if x > y:
                x = -1

        def qux3(y: int, y2: int, y3: int) -> object:
            nonlocal x
            nonlocal x2
            nonlocal x3
            if x > y:
                x = -1

        def qux4(y: int, y2: int, y3: int, y4: int) -> object:
            nonlocal x
            nonlocal x2
            nonlocal x3
            nonlocal x4
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"

    def baz5(self:"bar5", xx: [int], xx2: [int], xx3: [int], xx4: [int], xx5: [int]) -> str:
        global count
        x:int = 0
        x2:int = 0
        x3:int = 0
        x4:int = 0
        x5:int = 0
        y:int = 1
        y2:int = 1
        y3:int = 1
        y4:int = 1
        y5:int = 1

        def qux(y: int) -> object:
            nonlocal x
            if x > y:
                x = -1

        def qux2(y: int, y2: int) -> object:
            nonlocal x
            nonlocal x2
            if x > y:
                x = -1

        def qux3(y: int, y2: int, y3: int) -> object:
            nonlocal x
            nonlocal x2
            nonlocal x3
            if x > y:
                x = -1

        def qux4(y: int, y2: int, y3: int, y4: int) -> object:
            nonlocal x
            nonlocal x2
            nonlocal x3
            nonlocal x4
            if x > y:
                x = -1

        def qux5(y: int, y2: int, y3: int, y4: int, y5: int) -> object:
            nonlocal x
            nonlocal x2
            nonlocal x3
            nonlocal x4
            nonlocal x5
            if x > y:
                x = -1

        for x in xx:
            self.p = x == 2

        qux(0) # Yay! ChocoPy

        count = count + 1

        while x <= 0:
            if self.p:
                xx[0] = xx[1]
                self.p = not self.p
                x = x + 1
            elif foo("Long"[0]) == 1:
                self.p = self is None

        return "Nope"

print(bar().baz([1,2]))


