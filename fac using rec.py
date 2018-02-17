# Factorial of a number

def fac(n):
	if n==1 :
		return 1
	elif n==0 :
		return 1
	else:
		return(n*fac(n-1))

def main():
	a=int(input('\nEnter any number '))
	b= fac(a)
	print('\nThe factorial of ',a,' is ',b,'\n')

print('\n			  FACTORIAL OF A NUMBER		\n')
main()
