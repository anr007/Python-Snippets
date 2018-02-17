# fibonocci series

def fib(n):
	a, b = 0, 1
	for i in range(0,n):
		a, b = b, a+b
	return a

a=int(input('\nEnter the term which you want in the fibonocci series '))
print('\nThe ',a,' term in fibonocci series is ',fib(a))
