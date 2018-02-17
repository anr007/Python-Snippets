def fib(n):
	if n == 0: return 0
	if n == 1: return 1
	return fib(n-2) + fib(n-1)

a=int(input('\nEnter the term which you want in the fibonocci series '))
print('\nThe ',a,' term in fibonocci series is ',fib(a))
