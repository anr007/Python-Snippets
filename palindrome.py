a=list(input('\nEnter any word '))
print(a)
b=len(a)
c=b
j=0
for i in range(0,b):
	if a[i] == a[b-1] and a[i]!=' ':
		j=j+1
		b=b-1
if j==c:
	print('\nIt is a Palindrome')
else:
	print('\nIt is not a Palindrome')
