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
