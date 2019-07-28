# Part 1 of the Python Review lab
def hello_world():
	pass
	return("hello world")

def greet_by_name(name):
	return("hello "+str(name))
	pass

def encode(x):
	return(x*3953531)
	
def decode(y):
	return(y/3953531)
	pass

res = encode(5.5)
res2 = decode(res)

print(res2)