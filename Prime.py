#program for prime no.
n=int(input('Enter any Number '))
j=0
if n==1 or n==0:
 print(n,'is a not prime number')
else:
 for i in range(2,(n-1)):
  if n%i == 0:
   j+=j
 if j==0:
  print(n,'is a prime number')
 else:
  print(n,'is a not prime number')
 