try:
	for i in ['a','b','c']:
		print(i**2)
except TypeError:
	print("Invalid operation. Object is of string type, int type needed.")
