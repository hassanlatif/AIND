# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: We identify the naked twins in each unit and then remove the digits of the naked twins from their peers in that unit. The naked twin strategy is applied in conjunction with the eliminate and only choice strategy. The constraint propagation is used by combined application of these three reduction strategies unitl a solution is found or no further reductions can be made. The steps taken to solve the naked twin problem in the code is as follows:
1. For each box on the board identify twin peer of the box which has the same two digit value while discarding duplicate twins
2. Go through each unit and check if any of the above identified naked twins are in the unit. 
3. In case the unit has the naked twins, make sure that the twin digits are discarded from all other boxes in the unit.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: We add a diagonal unit to the sudoku units which becomes an additional contraint of the elimination strategy. The elimination strategy is used as part of the constraint propagation chain in addition to the naked twins and only choice strategy. The diagonal unit is created in the code by 'zipping' through row and column headers in the forward and backward directions.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.