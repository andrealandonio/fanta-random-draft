Fanta random draft
==============================

An easy CLI tool for managing a Fantacalcio draft based on user-defined player groups.

# Installation

You need to have Python 3 and the only required library is `numpy`. Here a list of command for installing libraries:

```bash
sudo apt-get install python3-tk
python3 -m pip install numpy
```

# Usage

Run the draft is very easy. You have to update `list.csv` with your changes and finally run the `main.py` file. After this, the process will ask you some information like the number of managers, their names and the initial budget for the draft. Inserted all these values the draft will start providing you the results grouped by manager.

Here how to run the program:

```bash
cd fanta-random-draft # or your project folder
/usr/bin/python main.py
```

# Tips

## Pots

The CSV file with the list of players must be organized grouping in 25 rows every pot. A pot represents a single draft extraction, so we will have 25 extractions according to the default Fantacalcio rules (3 goalkeepers, 8 defenders, 8 midfielders, 8 attackers).

Every row must have the number of players that corresponds to the number of managers and every player should contains 3 values separated by a comma. The name, the team and the price.

## Blocked player

You can "block" a player an assign it to a specific manager. For performing this operation you have to append to the player name the string "\*\*BLOCKED\*\*" and the number/index of the manager. For example:

```
Giroud**BLOCKED**3 
```

In this way the player defined above will be assigned to the manager at index 3. This operation will apply an extra price to the player. You can change this value directly in the `main.py` file changing the variable below: 

```py
blocker_player_extra = 30
```