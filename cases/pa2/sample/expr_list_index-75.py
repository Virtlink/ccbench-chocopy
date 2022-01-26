x:[int] = None
y:int = 0
z:[bool] = None
o:object = None

x = [1, 2, 3]
z = [False, True]

y = x[[[Literal]]]
x[0] = 1
z[1] = z[0]
o = x[1]
