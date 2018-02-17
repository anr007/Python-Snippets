# concordance
# prints word , line no.s in which it appears in an alphabetical order

a=input('Enter any text (type quit to end) \n')
b=a.lower()
d={}
i=1
while b!='quit':
	l=b.split()
	for w in l:
# below statement assigns previous value if present or creates a new list m
		m= d.get(w,[])
		if i not in m:
			m.append(i)
		d[w]=m
	i=i+1
	a=input()
	b=a.lower()

print('\n')
for k in sorted(d.keys()):
	print(k ,':', d[k])
	
		
	