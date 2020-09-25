from random import randint

moves = ["Rock", "Paper", "Scissors"]
computer = moves[randint(0,2)]
player = input("Rock, Paper, Scissors?")
print("Computer move:", computer)
print("Player move:",player)
if player == computer:
    print("Tie!")
elif player == "Rock":
    if computer == "Paper":
        print("You lose!")
    else:
        print("You win!")
elif player == "Paper":
    if computer == "Scissors":
        print("You lose!")
    else:
        print("You win!")
elif player == "Scissors":
    if computer == "Rock":
        print("You lose!")
    else:
        print("You win!")
else:
    print("Only Rock, Paper, Scissors are accepted.")


