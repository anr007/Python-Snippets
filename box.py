# prints a box of give h,w

h=int(input("height "))
w=int(input("width "))
print("@"*w)
for i in range(1,h-1):
    print("@"," "*(w-4),"@") # w-4 refers to the value for which the size of n '@' values equal to n " " (empty spaces).
print("@"*w)
