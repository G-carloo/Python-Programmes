import random
Number = random.randint(1, 100)
print(Number)
Number_of_Guesses = 0
while Number_of_Guesses < 10:
    Guess = int(input("Guess the number:\n"))
    Number_of_Guesses = Number_of_Guesses +1

 if Number_of_Guesses == 10:
     print("You lose")
        break

if Guess == Number:
    print("You win, although it took", Number_of_Guesses,"tries")
        break

if  Guess >= Number:
        print("Too high my man")
    Number_of_Guesses = Number_of_Guesses +1

if Guess <= Number:
    print("Too low my man")
 Number_of_Guesses = Number_of_Guesses +1

else:
    print("You lose")


