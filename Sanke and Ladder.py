import random

snakes = {22: 6, 45: 30, 96: 64}
ladders = {7: 24, 21: 47, 42: 90, 40: 60}

player_pos = {1: 0, 2: 0}

def roll_dice():
    return random.randint(1, 6)

def update_position(player, roll):
    pos = player_pos[player] + roll

    if pos > 100:
        print(f"Player {player} rolled {roll}, but move exceeds 100. Staying at {player_pos[player]}.")
        return

    print(f"Player {player} rolled a {roll} and moved to {pos}")

    if pos in snakes:
        print(f"Oops! Snake bite at {pos}. Down to {snakes[pos]}")
        pos = snakes[pos]

    elif pos in ladders:
        print(f"Yay! Ladder climb from {pos} to {ladders[pos]}")
        pos = ladders[pos]

    player_pos[player] = pos

def print_status():
    print(f"Player 1: {player_pos[1]}")
    print(f"Player 2: {player_pos[2]}")

def play_game():
    current_player = 1
    while True:
        print("\n-------------------------")
        print(f"Enter player no: {current_player}")
        input("Press Enter to roll dice...")
        dice = roll_dice()
        print(f"Dice score: {dice}")

        update_position(current_player, dice)
        print_status()

        if player_pos[current_player] == 100:
            print(f"\n Player {current_player} wins the game! ")
            break

        current_player = 2 if current_player == 1 else 1

play_game()
