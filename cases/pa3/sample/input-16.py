# Test of 'input' function.

s: str = ""

[[ID]] = input()
while len(s) > 0:
    print(s)
    s = input()
