# A resizable list of integers
class Vector(object):
    $ClassBody

# A faster (but more memory-consuming) implementation of vector
class DoublingVector(Vector):
    doubling_limit:int = 1000

    # Overriding to do fewer resizes
    def increase_capacity(self:"DoublingVector") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

# Makes a vector in the range [i, j)
def vrange(i:int, j:int) -> Vector:
    v:Vector = None
    v = DoublingVector()
    
    while i < j:
        v.append(i)
        i = i + 1

    return v

# Sieve of Eratosthenes (not really)
def sieve(v:Vector) -> object:
    i:int = 0
    j:int = 0
    k:int = 0

    while i < v.length():
        k = v.get(i)
        j = i + 1
        while j < v.length():
            if v.get(j) % k == 0:
                v.remove_at(j)
            else:
                j = j + 1
        i = i + 1

# Input parameter
n:int = 50

# Data
v:Vector = None
i:int = 0

# Crunch
v = vrange(2, n)
sieve(v)

# Print
while i < v.length():
    print(v.get(i))
    i = i + 1

