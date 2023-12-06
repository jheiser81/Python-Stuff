def print_map():
    print(f"{row1}\n{row2}\n{row3}\n")

# Setting up the lists
row1 = ["_","_","_"]
row2 = ["_","_","_"]
row3 = ["_","_","_"]
treasure_map = [row1, row2, row3]

# Treasure Randomizer
import random
treasure_row = random.randint(0,2)
treasure_column = random.randint(0,2)

# Messages to the user
print("Welcome to the Treasure Map!")
print("You are on a deserted island and there is a treasure hidden somewhere.")
print("The treasure will be buried in a random location. You have to find the treasure within 5 attempts.")
print("Each place on the map is represented by a letter and a number, in the format of: A1, B3, C2, etc.")
print("Let's begin! Here is the map: \n")
print_map()

# User input
dig_count = 0 # Keep track of the number of digs
previous_digs = [] # Keep track of previous dig locations entered by the user

while dig_count < 5:
    dig_location = input("Enter the column letter and row number of where you want to dig: ")
    column_letter = dig_location[0].upper()
    row_number = int(dig_location[1]) - 1

    # Column Index
    column_letters = ["A", "B", "C"]
    column_index = column_letters.index(column_letter)
    
    # Check if location is valid or if location was already selected
    if dig_location in previous_digs:
        print("You have already dug here. Try again!\n")
        print_map()
        continue 
    # Checks if location was already selected
    elif column_index < 0 or column_index > 2:
        print("Invalid location. Try again!\n")
        print_map()
        continue
    # Checks if location is valid (within the map)
    else:
        previous_digs.append(dig_location)
        dig_count += 1
    # Adds dig_location to the list of previous digs, and increments dig_count by 1

    # Check if treasure is found
    if row_number == treasure_row and column_index == treasure_column:
        treasure_map[row_number][column_index] = "X"
        print(f"The treasure was buried at {column_letters[treasure_column]}{treasure_row + 1}.")
        print("You found the treasure! Congratulations!\n")
        print_map()
        break
    else:
        treasure_map[row_number][column_index] = "O"
        print("\nYou didn't find the treasure. Try again!")
        dig_count += 1
        print(f"You have {5 - dig_count} attempts left.\n")
        print_map()
        
    if dig_count == 5:
        print("You have run out of attempts.")
        treasure_map[treasure_row][treasure_column] = "X"
        print(f"The treasure was buried at {column_letters[treasure_column]}{treasure_row + 1}.\n")
        print_map()
        print("Game Over.")
        break
    
# use functions to print map, DRY
# use while loop to repeat game?
# implement logic for when user enters invalid input, or enters the same location twice



















