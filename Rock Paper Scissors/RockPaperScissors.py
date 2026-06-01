import random
choices = ["rock","paper","scissors"]
player = ""
p_wins = 0
c_wins = 0
print("Rock crushes scissors. Scissors cut paper. Paper covers rock.")
while p_wins != 3 and c_wins != 3:
    player = input("Enter a choice (rock , paper, scissors(place all choices in LOWER CASE only)): ")
    computer = random.choice(choices)
    print("You play " + player + ", and the computer plays " + computer + ".")
    if player == computer:
        print("Its a tie!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
            p_wins += 1
        else:
            print("Computer wins")
            c_wins += 1
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
            p_wins += 1
        else:
            print("Computer wins!")
            c_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("You win!")
            p_wins += 1
        else:
            print("Computer wins!")
            c_wins += 1
    else:
        print("ERROR")
if (p_wins == 3):
    print("You are the final winner!")
else:
    ("You lose!")
