a:str = "Hello"
b:str = "World"
c:str = "ChocoPy"

def cat2(a:str, b:str) -> str:
    return a + b

[[Definition]]

print(cat2(a, b))
print(cat2("", c))
print(cat3(a, " ", c))
print(len(a))
print(len(cat2(a,a)))
print(len(cat2("","")))
