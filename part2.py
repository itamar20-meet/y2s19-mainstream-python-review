# Part 2 of the Python Review lab.
def check_prime(x,y):
	for i in range(2,x):
		if(x % i) == 0:
			pass
       	else :
			x+=1
	for i in range(2,y):
				if (y % i) == 0:
					pass
				else:
					y+=1
	return x,y



def encode(x, y):
		check_prime (x,y)
		if 1 < y < 250 and 500 < x < 1000:
			return x*y
		else:
			print("Invalid input:Outside range")
			return None 	

	
	
       			
       				
       			

	

	
def decode(coded_message):
	encode()