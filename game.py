import random
level=input("Choose Difficulty LEVEL(E,M,H):")
if(level=="E"):
    target = random.randint(1,20)
if(level=="M"):
    target = random.randint(1,40)
if(level=="H"):
    target = random.randint(1,60)    
    
for i in range(0,5,1) :
    userChoice = int(input("Guess the target OR select 0 for quit= "))
    if (userChoice==0):
        break
    if (userChoice==target):
        print("YOU WON!!")
        break
    elif(userChoice < target):
        print("You selected small no...Guess bigger no. TRY AGAIN!")
    else:
        print("You selected larger no...Guess smaller no. TRY AGAIN!")  
    print((4-i),"chances left")
        
if(userChoice==target):
    print("Congratulations")
else:
    print("OOPS! You Lost")
    print("The Correct no is",target)
print("---GAME OVER---")        
        
         
    