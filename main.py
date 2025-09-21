import random

def greeting():
  return "Hi, want to play a game of rock paper scissors?"

response = greeting ()
print(response)

def line_break():
  return "------------------------------------------------------"

response = line_break ()
print(response)

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  output = ["rock", "paper", "scissors"]
  computer_choice = random.choice(output)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

choices = get_choices()
print(choices)

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    response = "It's a tie!"
    print(response)
  elif player == "rock" and computer == "scissors":
    response = "Rock smashes scissors! You win!"
    print(response)
  elif player == "scissors" and computer == "paper":
    response = "Scissors cuts paper! You win!"
    print(response)
  elif player == "paper" and computer == "rock":
    response = "Paper covers rock! You win!"
    print(response)
  else:
    response = "You lose."
    print(response)

result = check_win(choices["player"], choices["computer"])
print(response)