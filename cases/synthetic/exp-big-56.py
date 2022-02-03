# Compute x**y
def exp(x: int, y: int) -> int:
    a: int = 0
    a2: int = 0
    a3: int = 0
    a4: int = 0
    a5: $ID = 0
    def f(i: int) -> int:
        nonlocal a
        nonlocal a2
        nonlocal a3
        nonlocal a4
        nonlocal a5
        def geta() -> int:
            return a
        if i <= 0:
            return geta()
        else:
            a = a * x
            a2 = a * x
            a3 = a * x
            a4 = a * x
            a5 = a * x
            return f(i-1)
    a = 1
    a2 = 1
    a3 = 1
    a4 = 1
    a5 = 1
    return f(y)

def exp2(x: int, y: int, x2: int, y2: int) -> int:
    a: int = 0
    a2: int = 0
    a3: int = 0
    a4: int = 0
    a5: int = 0
    def f(i: int) -> int:
        nonlocal a
        nonlocal a2
        nonlocal a3
        nonlocal a4
        nonlocal a5
        def geta() -> int:
            return a
        if i <= 0:
            return geta()
        else:
            a = a * x
            a2 = a * x
            a3 = a * x
            a4 = a * x
            a5 = a * x
            return f(i-1)
    a = 1
    a2 = 1
    a3 = 1
    a4 = 1
    a5 = 1
    return f(y)

def exp3(x: int, y: int, x2: int, y2: int, x3: int, y3: int) -> int:
    a: int = 0
    a2: int = 0
    a3: int = 0
    a4: int = 0
    a5: int = 0
    def f(i: int) -> int:
        nonlocal a
        nonlocal a2
        nonlocal a3
        nonlocal a4
        nonlocal a5
        def geta() -> int:
            return a
        if i <= 0:
            return geta()
        else:
            a = a * x
            a2 = a * x
            a3 = a * x
            a4 = a * x
            a5 = a * x
            return f(i-1)
    a = 1
    a2 = 1
    a3 = 1
    a4 = 1
    a5 = 1
    return f(y)

def exp4(x: int, y: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) -> int:
    a: int = 0
    a2: int = 0
    a3: int = 0
    a4: int = 0
    a5: int = 0
    def f(i: int) -> int:
        nonlocal a
        nonlocal a2
        nonlocal a3
        nonlocal a4
        nonlocal a5
        def geta() -> int:
            return a
        if i <= 0:
            return geta()
        else:
            a = a * x
            a2 = a * x
            a3 = a * x
            a4 = a * x
            a5 = a * x
            return f(i-1)
    a = 1
    a2 = 1
    a3 = 1
    a4 = 1
    a5 = 1
    return f(y)

def exp5(x: int, y: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int, x5: int, y5: int) -> int:
    a: int = 0
    a2: int = 0
    a3: int = 0
    a4: int = 0
    a5: int = 0
    def f(i: int) -> int:
        nonlocal a
        nonlocal a2
        nonlocal a3
        nonlocal a4
        nonlocal a5
        def geta() -> int:
            return a
        if i <= 0:
            return geta()
        else:
            a = a * x
            a2 = a * x
            a3 = a * x
            a4 = a * x
            a5 = a * x
            return f(i-1)
    a = 1
    a2 = 1
    a3 = 1
    a4 = 1
    a5 = 1
    return f(y)

# Input parameter
n:int = 42
n2:int = 42
n3:int = 42
n4:int = 42
n5:int = 42

# Run [0, n]
i:int = 0
i2:int = 0
i3:int = 0
i4:int = 0
i5:int = 0

# Crunch
while i <= n:
    print(exp(2, i % 31))
    i = i + 1