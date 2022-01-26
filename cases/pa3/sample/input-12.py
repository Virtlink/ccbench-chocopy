# Test of 'input' function.

s: str = ""

 input()
while len(s) > 0:
    print(s)
    s = input()
