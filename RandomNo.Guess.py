import random

x = random.randrange(0, 10)
Guesses=0

while Guesses < 3:
    Guess = int(input("Guess The Number:\n"))
    Guesses +=1
    if  Guess == x:
     break
if Guess == x:
    print("Winner Winner, Chicken Dinner")

else :
    print("You lose. LOSER")

