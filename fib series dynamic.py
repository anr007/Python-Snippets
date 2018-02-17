# dynamic programming
# stores already counted values in a dictionary file and speeds up the execution

fibs = {0:0, 1:1}

def rfib(n):
	global fibs
	if n not in fibs.keys():
		fibs[n] = rfib(n-2) + rfib(n-1)
	return fibs[n]

a=int(input('\nEnter the term which you want in the fibonocci series '))
print('\nThe ',a,' term in fibonocci series is ',rfib(a))
