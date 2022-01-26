# Test of 'input' function.

s: [[ID]] = ""

s = input()
while len(s) > 0:
    print(s)
    s = input()
