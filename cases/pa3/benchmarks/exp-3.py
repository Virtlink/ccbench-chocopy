# Compute x**y
$FuncDef

# Input parameter
n:int = 42

# Run [0, n]
i:int = 0

# Crunch
while i <= n:
	print(exp(2, i % 31))
	i = i + 1