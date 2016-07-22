def gensquares(N):
	for n in range(10):
		yield n**2

for x in gensquares(10):
	print(x)
