# Get the n-th prime starting from 2
[[Definition]] # Never happens

def is_prime(x:int) -> bool:
    div:int = 2
    while div < x:
        if x % div == 0:
            return False
        div = div + 1
    return True

# Input parameter
n:int = 15

# Run [1, n]
i:int = 1

# Crunch
while i <= n:
    print(get_prime(i))
    i = i + 1
