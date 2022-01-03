i = 1
while i <= 3:
    guess = input("Guess the Secret No. ")
    i += 1
    if guess == "9":
        print("You Won the Game..!")
        break
else:
    print("Sorry..! You Lose the Game")


