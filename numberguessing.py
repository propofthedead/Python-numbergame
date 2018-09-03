import random
print("\n Welcome to 'Guess my Number!'")
print("\nI'm thinking of a number between 1 and 100")
print("Try to guess it in as few attempts as possible")

thenumber = random.randint(1,100)

guess= int(input("Take a guess: "))
tries=1

while thenumber != guess :
    if guess>thenumber:
        print("Lower... \n")

    elif guess<thenumber:
        print("Higher... \n")

    guess= int(input("Take a guess: "))
    tries+=1

print("You guess the number correct ", thenumber," \n")
print("And it only took you, ",tries, " tries \n")


input("Press the enter key to exit")
