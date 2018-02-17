import random

print("The rules of craps are as follows:","\n")
print("A player rolls a pair of dice. If the sum of dice is either 7 or 11 on the first throw, the player wins.")
print("If the sum is 2, 3 or 12 on the first throw, the playerloses.")
print("Any other sum becomes the players “point”.")
print("To win, the player must continue rolling the dice until a roll matches the point.")
print("This is termed “making the point”.")
print("If the player rolls a seven before making the point the player loses.")



print("\n","Press any to roll a pair of dice ")
input()
d1=random.randint(1,6) # generates a random int of range b/w 1 & 6 with equal probability
d2=random.randint(1,6)
p=d1+d2
if p==7 or p==11:
 print("\n"," You Won the Game")
 exit(0)
elif p==2 or p==3 or p==12:
 print("\n","You lost the game")
 exit(1)
else:
 print("\n"," Your Point is ",p)
for i in range(1,8):
 print("\n"," Press any to roll a pair of dice")
 input()
 d1=random.randint(1,6)
 d2=random.randint(1,6)
 r=d1+d2
 print(r)
 if r==p:
  print("\n","You won the game")
  exit(0)
print("\n","your are out of chances","You lost the game")



