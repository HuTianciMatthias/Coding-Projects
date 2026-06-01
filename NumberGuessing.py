import random
low = 1
high = 100
tries_left = 0
tries_took = 0
secret_num = random.randint(1 , 100)
guess_num = 0
difficulty = input("Please choose your level of difficulty: Easy(E) / Medium(M) / Hard(H): ")
if difficulty.lower() == "e":
    tries_left = 15
elif difficulty.lower() == "m":
    tries_left = 10
else:
    tries_left = 5
print("You have " + str(tries_left) + " tries in total.")
print("Welcome to GUESS MY NUMBER.")
while guess_num != secret_num and tries_left > 0:
    tries_left -= 1
    tries_took += 1
    guess_num = int(input("Guess the number: (" + str(low) + " - " + str(high) + "):"))
    if(guess_num > 100 or guess_num < 1):
        print("Please enter a valid number (1 - 100): ")
    elif(guess_num > secret_num):
        print("Guess number is too high")
        high = guess_num
    elif(guess_num < secret_num):
        print("Guess number is too low")
        low = guess_num
    elif(guess_num == secret_num):
        print("Bingo! You took " + str(tries_took) + " tries to guess it right!")
if (tries_left == 0 and secret_num != guess_num):
    print("Sorry buddy, you have used up all the tries. Please try again")
