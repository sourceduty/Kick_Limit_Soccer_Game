### Kick_Limit_Soccer_Game

⚽ The classic game of soccer with limited ball kicking rules.
#
### CONCEPT

Classic Soccer Rules:

Soccer games are started with a coin toss. The captain of the away team calls heads or tails, and the winning captain gets to choose whether their team will take the first kickoff. In the second half, the kickoff is taken by the side that did not take it in the first.

Each soccer team consists of 11 soccer players, one of which is the goalkeeper. A soccer game is split into two 45 minute halves, with a break in between for halftime. Each team scores goals by getting the ball into the other team’s net. The team with the most goals at the end of the game wins.

#

Kick Limit Soccer Rules:

Each team scores goals with a limited amount of ball kicks. The team with the most goals at the end of the limited game wins.
#
### LICENSE

Copyright (C) 2023,  Sourceduty - All Rights Reserved.

THE CONTENTS OF THIS PROJECT ARE PROPRIETARY.
#
### DEVELOPMENT

ChatGPT Concept:

```
import random

def main():
    print("Welcome to the Text-based Soccer Game!")
    team1_name = input("Enter the name of Team 1: ")
    team2_name = input("Enter the name of Team 2: ")
    total_kicks = int(input("Enter the number of kicks per team: "))

    team1_score = 0
    team2_score = 0

    for kick in range(total_kicks):
        print(f"\nKick {kick + 1} - {team1_name}'s Turn")
        team1_score += take_kick(team1_name)

        print(f"\nKick {kick + 1} - {team2_name}'s Turn")
        team2_score += take_kick(team2_name)

    print("\nGame Over!")

    if team1_score == team2_score:
        print("It's a tie! Final score: {} - {}.".format(team1_score, team2_score))
    elif team1_score > team2_score:
        print(f"{team1_name} wins with a score of {team1_score} - {team2_score}.")
    else:
        print(f"{team2_name} wins with a score of {team2_score} - {team1_score}.")

def take_kick(team_name):
    input("Press Enter to take a kick...")
    goal = random.choice([True, False])  # Randomly decide if it's a goal or not
    if goal:
        print(f"{team_name} scored a goal!")
        return 1
    else:
        print(f"{team_name}'s kick missed.")
        return 0

if __name__ == "__main__":
    main()

```
#
