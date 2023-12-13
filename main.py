import numpy as np
from manager import Manager
from player import Player

# Define constants and variables
row_separator_big = "#######################################################"
row_separator_medium = "------------------------"
row_separator_small = "-"
blocker_player_extra = 30

# Display logo
print(row_separator_big)
print("Fanta random draft")
print(row_separator_big)

# Ask initial budget
initial_budget = int(input("Enter the initial budget for every manager: "))

# Ask number of managers
managers_number = int(input("Enter the number of managers: "))

# Import list (from CSV)
pots = []
for line in open("list.csv"):
    pot_players = []
    row_players = line.split(",")
    for index in range(int(len(row_players) / 3)):
        player = Player(row_players[index * 3].strip(), row_players[index * 3 + 1].strip(), int(row_players[index * 3 + 2]))
        pot_players.append(player)
    pots.append(pot_players)

# Manage managers
managers = np.empty(managers_number, dtype = Manager)
for index in range(managers_number):
    manager_name = input("Enter manager " + str(index + 1) + " name: ")
    manager = Manager(manager_name.strip(), initial_budget)
    managers[index] = manager

# Start drafting
for index in range(len(pots)):
    print(row_separator_small + " Managing POT " + str(index + 1))

    # Loop draft pots
    pot_players = pots[index]
        
    # Set managers to manage
    managers_to_manage = []
    for index in range(managers_number):
        managers_to_manage.append(index)

    # Check if manager do not need extraction
    position = 0    
    pot_players_to_delete = []
    for pot_player in pot_players:
        if (pot_player.name.find('**BLOCKED**') != -1):
            # Get manager who blocked the player
            blocked_manager = int(pot_player.name.split("**")[2])
            pot_manager = managers[blocked_manager]

            # Increase blocked player price and update real player name
            pot_player.price = pot_player.price + blocker_player_extra
            pot_player.name = pot_player.name.split("**")[0]

            # Assign player to manager and update manager
            pot_manager.add_player(pot_player)
            managers[blocked_manager] = pot_manager

            # Set player and manager to not manage during the current pot
            pot_players_to_delete.append(position)
            
            # Remove managers already managed
            for index in managers_to_manage:
                temp_manager = managers[index]
                if (temp_manager.name == pot_manager.name):
                    managers_to_manage.remove(index)
                    break

            print(row_separator_small + " Assign player " + pot_player.name + " to " + pot_manager.name + " for " + str(pot_player.price))
        
        # Go next pot player
        position = position + 1

    # Remove blocked player (already managed) from pot
    for index in sorted(pot_players_to_delete, reverse=True):
        del pot_players[index]

    # Loop managers to manage
    for index in managers_to_manage:
        # Retrieve manager 
        pot_manager = managers[index]

        # Extract random player
        extracted_player = np.random.randint(0, len(pot_players))
        pot_player = pot_players[extracted_player]

        # Check if player can be assigned by counting remaining budget and remaining players to buy
        if (int(pot_player.price) < (pot_manager.get_remaining_budget() - pot_manager.get_remaining_players())):
            # Add player to current manager
            pot_manager.add_player(pot_player)

            # Remove manager and player from pot (for make it unavailable for next rounds)
            del pot_players[extracted_player]
        else:
            pot_manager.add_player(Player("Unknown", "Unknown", 1))
        
        # Add manager to managers array
        managers[index] = pot_manager

print(row_separator_big)
print("Result")
print(row_separator_big)

# Show managers
for manager in managers:
    manager.show() 
    print(row_separator_medium)
