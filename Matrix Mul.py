r1=int(input("Enter the no.of rows in matrix:1 "))
c1=int(input("Enter the no.of coloumns in matrix:1 "))
r2=int(input("Enter the no.of rows in matrix:2 "))
c2=int(input("Enter the no.of coloumns in matrix:2 "))
if (c1 == r2):
    print("Enter the %d elements in matrix:1 "%(r1*c1))
else :
    print("Matrix Multiplication is not possible")
    quit(1)

m1=[0]*r1
for i in range(0,r1):
    m1[i]=[0]*c1
# do not use m1=[[0]*c1]*r1 as it creates copies of same coloumn & changing one element in one coloumn changes elements of identical position in other coloumns also.
for i in range(0,r1):
    for j in range(0,c1):
        m1[i][j]=int(input())
print("Enter the %d elements in matrix:2 "%(r2*c2))
m2=[0]*r2
for i in range(0,r2):
    m2[i]=[0]*c2

for i in range(0,r2):
    for j in range(0,c2):
        m2[i][j]=int(input())

m3=[0]*r1
for i in range(0,r1):
    m3[i]=[0]*c2

for i in range(0,r1):
    for j in range(0,c2):
        for k in range(0,c1):
            m3[i][j] = m3[i][j] + m1[i][k] * m2[k][j]

print("\n")
print("The product of Matrix 1 & Matrix 2 is ")
for i in range(0,r1):
    print(m3[i])

