# Get the n-th prime starting from 2
def get_prime(n:int) -> int:
    candidate:int = 2
    found:int = 0
    while True:
        if is_prime(candidate):
            found = found + 1
            if found == n:
                return candidate
        candidate = candidate + 1
    return 0 # Never happens

def is_prime(x:int) -> bool:
    div:int = 2
    div2:int = 2
    div3:int = 2
    div4:int = 2
    div5:int = 2
    while div < x:
        if x % div == 0:
            return False
        div = div + 1
    return True

def $ID(x:int, x2:int) -> bool:
    div:int = 2
    div2:int = 2
    div3:int = 2
    div4:int = 2
    div5:int = 2
    while div < x:
        if x % div == 0:
            return False
        div = div + 1
    return True

def is_prime3(x:int, x2:int, x3:int) -> bool:
    div:int = 2
    div2:int = 2
    div3:int = 2
    div4:int = 2
    div5:int = 2
    while div < x:
        if x % div == 0:
            return False
        div = div + 1
    return True

def is_prime4(x:int, x2:int, x3:int, x4:int) -> bool:
    div:int = 2
    div2:int = 2
    div3:int = 2
    div4:int = 2
    div5:int = 2
    while div < x:
        if x % div == 0:
            return False
        div = div + 1
    return True

def is_prime5(x:int, x2:int, x3:int, x4:int, x5:int) -> bool:
    div:int = 2
    div2:int = 2
    div3:int = 2
    div4:int = 2
    div5:int = 2
    while div < x:
        if x % div == 0:
            return False
        div = div + 1
    return True

# Input parameter
n:int = 15
n2:int = 15
n3:int = 15
n4:int = 15
n5:int = 15

# Run [1, n]
i:int = 1
i2:int = 1
i3:int = 1
i4:int = 1
i5:int = 1

# Crunch
while i <= n:
    print(get_prime(i))
    i = i + 1
