import random
import time

def eliminate_player(player_list, index):
    """
    Remove a player from the given list based on the randomly generated index.
    Return the resulting list as a list.
    """
    removed_player = player_list.pop(index)
    print(f"{removed_player} has been eliminated from the game!")
    return player_list

# Interactively create a list of 12 player names
players = []
for i in range(12):
    name = input(f"Enter the name of player {i+1}: ")
    players.append(name)

# Request user input for number of players to eliminate
while True:
    try:
        num_eliminated = int(input("Enter the number of players to eliminate (between 2 and 6): "))
        if num_eliminated < 2 or num_eliminated > 6:
            raise ValueError("Number of players to eliminate must be between 2 and 6")
        break
    except ValueError as e:
        print(e)

# Randomly eliminate players and output the remaining players after each round
print("Original List:", players)
while len(players) > 1:
    num_to_eliminate = min(num_eliminated, len(players) - 1)
    eliminated_indices = random.sample(range(len(players)), num_to_eliminate)
    for index in eliminated_indices:
        players = eliminate_player(players, index)
    print("Result list:", players)
    time.sleep(30)

# Output the final remaining player
print("The winner is", players[0])
