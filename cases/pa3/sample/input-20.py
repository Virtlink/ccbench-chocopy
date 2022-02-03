# Test of 'input' function.

s: str = ""

s = $ID()
while len(s) > 0:
    print(s)
    s = input()
