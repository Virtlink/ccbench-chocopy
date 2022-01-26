# Test of 'input' function.

s: str = [[Literal]]

s = input()
while len(s) > 0:
    print(s)
    s = input()
