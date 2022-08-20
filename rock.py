import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors:")


option = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
choices = {"player": player_choice, "computer": computer_choice}
return choices
choices = get_choices()
print(choices)


food = ["pizza", "carrot", "eggs"]
dinner = random.choice(food)
