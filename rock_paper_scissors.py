import random

SCISSORS = "scissors"
PAPER = "paper"
ROCK = "rock"
SYLVAIN = "sylvainlebg"

MY_SCORE = 0
IA_SCORE = 0
MAX_POINTS = 5

CHOICE = "Make your choice: |Rock - Paper - Scissors|:"

while MAX_POINTS > MY_SCORE or MAX_POINTS > IA_SCORE:

    possible_choices = [ROCK, PAPER, SCISSORS]
    while True:
        player_choice = input(CHOICE)
        if player_choice in (possible_choices[0], possible_choices[1], possible_choices[2], possible_choices[3]):
            break

    if player_choice == SYLVAIN:
        print("You win!")
        break

    choix_ia = random.choice(possible_choices)

    print(f"You chose {player_choice}. IA chose {choix_ia}")

    if (player_choice == PAPER and choix_ia == ROCK) \
            or (player_choice == ROCK and choix_ia == SCISSORS) \
            or (player_choice == SCISSORS and choix_ia == PAPER):
        MY_SCORE += 1
        print(f"You won! Score is {MY_SCORE} - {IA_SCORE}")

    elif (player_choice == PAPER and choix_ia == SCISSORS) \
            or (player_choice == ROCK and choix_ia == PAPER) \
            or (player_choice == SCISSORS and choix_ia == ROCK):
        IA_SCORE += 1
        print(f"You lost! Score is {MY_SCORE} - {IA_SCORE}")

    else:
        print(f"You made the same choice, tie! Score is {MY_SCORE} - {IA_SCORE}")

    if MAX_POINTS in (MY_SCORE, IA_SCORE):
        break
