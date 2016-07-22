from math import sqrt

def ask():
	x = True	
	while x:
		d = input("Input an integer: ")		
		try:		
			d_int = int(d)
			print("Thank you, you number squared is: " + str(d_int**2))
		except TypeError:
			print("An error occured! Please try again!")
		except ValueError:
			print("An error occured! Please try again!")

ask()

