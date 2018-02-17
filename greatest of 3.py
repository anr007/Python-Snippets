# Greatest of 3 numbers

a=[]
print('Enter any 3 numbers')
for i in range(3):
	a.append(int(input()))

# We can also use a fixed number list like a=[none]*3 and use a[i] int for loop to assign
# input values.

if a[0]>a[1] and a[1]>a[2]:
	print('The greatest number is ',a[0])
elif a[0]<a[1] and a[1]>a[2]:
	print('The greatest number is ',a[1])
elif a[0]<a[1] and a[1]<a[2]:
	print('The greatest number is ',a[2])
elif a[0]>a[1] and a[1]<a[2]:
	if a[0]>a[2]:
		print('The greatest number is ',a[0])
	else:
		print('The greatest number is ',a[2])
	

