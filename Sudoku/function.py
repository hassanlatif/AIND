from utils import *

input_values = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

grid_values = grid_values(input_values)

#display(grid_values)

print(len(grid_values))
print(len(peers))

solved_values = [box for box in grid_values.keys() if len(grid_values[box]) == 1]

#print("                                  ")

#print(solved_values)

for box in solved_values:
	digit = grid_values[box]
	for peer in peers[box]:
		grid_values[peer] = grid_values[peer].replace(digit,'')


#return grid_values
print(grid_values)



def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """