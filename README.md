# Kakuro

## Overview

This Python script implements a Kakuro solver using the Constraint Satisfaction Problem (CSP) paradigm, backtracking algorithm, and Minimum Remaining Values (MRV) heuristic. Kakuro is a number puzzle game, similar to Sudoku, where players fill a grid with numbers based on given clues.

## Features

- **CSP Approach**: Utilizes the  CSP methodology to model and solve the Kakuro puzzle. CSP involves defining variables, domains, and constraints to find a consistent assignment of values.

- **Backtracking Algorithm**: Employs the backtracking algorithm to explore the solution space efficiently. Backtracking is a systematic trial-and-error approach to finding a solution.

- **Minimum Remaining Values (MRV) Heuristic**: Applies the MRV heuristic to prioritize variables with the fewest remaining possible values. This helps in selecting the most promising variable at each step.

## Usage

1. **Requirements**: Ensure you have Python installed on your system.

2. **Clone the Repository**:

    ```bash
    git clone https://github.com/MobinaAfsharii/kakuro
    cd kakuro
    ```

3. **Run the Solver**:

    ```python
    python main.py
    ```

4. **Input Format**:

    Provide the Kakuro puzzle as input in a suitable format. This may include the size of the grid, initial values, and clue numbers.

    Example Input:

    ```python
    """#|#     #|#     #|#     #|17    #|28    #|#     #|#

       #|#     #|#     16|27   0|0     0|0     #|17    #|17

       #|#     27|11   0|0     0|0     0|0     0|0     0|0

       3|#     0|0     0|0     19|14   0|0     0|0     0|0

       34|#    0|0     0|0     0|0     0|0     0|0     #|17

       #|#     30|#    0|0     0|0     0|0     0|0     0|0

       #|#     3|#     0|0     0|0     16|#    0|0     0|0"""
    ```

5. **Output**:

    The solver will output the solved Kakuro grid.

## Implementation Details

- **Variable Definition**: Define variables representing the cells in the Kakuro grid that need to be filled.

- **Domain Definition**: Specify the possible values that can be assigned to each variable (e.g., numbers 1 to 9).

- **Constraint Definition**: Define constraints based on Kakuro rules, ensuring that each row and column satisfies the specified clues.

- **Backtracking with MRV**: Implement the backtracking algorithm, selecting variables based on the MRV heuristic. Apply constraints and backtrack when needed.

## Example

```python
from kakuro.board import Board
from tests import Test

board_scheme = """
#|#     #|#     #|#     #|17    #|28    #|#     #|#

#|#     #|#     16|27   0|0     0|0     #|17    #|17

#|#     27|11   0|0     0|0     0|0     0|0     0|0

3|#     0|0     0|0     19|14   0|0     0|0     0|0

34|#    0|0     0|0     0|0     0|0     0|0     #|17

#|#     30|#    0|0     0|0     0|0     0|0     0|0

#|#     3|#     0|0     0|0     16|#    0|0     0|0
"""

if __name__ == "__main__":
    board = Board(board_scheme)
    board.optimize()
    board.print_values()

```
