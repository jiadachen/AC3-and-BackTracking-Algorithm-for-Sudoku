# AC3 and BackTracking Algorithm for Sudoku
## Spec

This is a project for constraint satisfaction problems, where AC-3 and backtracking algorithms are implemented to solve Sudoku puzzles. The objective of the game is just to fill a 9 x 9 grid with numerical digits so that each column, each row, and each of the nine 3 x 3 sub-grids (also called boxes) contains one of all of the digits 1 through 9. A demo of the game is available at sudoku.com.

In a Sudoku puzzle, there are 81 variables in total, i.e. the tiles to be filled with digits. Each variable is named by its row and its column, and must be assigned a value from 1 to 9, subject to the constraint that no two cells in the same row, column, or box may contain the same value.

A Sudoku board is implemented with a Python dictionary. The keys of the dictionary will be the variable names, each of which corresponds directly to a location on the board. In other words, variable names Al through A9 are used for the top row (left to right), down to I1 through I9 for the bottom row. The number zero is used to indicate tiles that have not yet been filled.

The program will be executed as follows:
```$ python driver.py <input_string>```

The sudokus_start.txt contains hundreds of sample Sudoku puzzles to be solved. Each Sudoku puzzle is represented as a single line of text, which starts from the top-left corner of the board, and enumerates the digits in each tile, row by row. For example, the first Sudoku board in sudokus_start.txt is represented as the string:
```003020600900305001001806400008102900700000008006708200002609500800203009005010300```

When executed as above, replacing "<input_string>" with any valid string representation of a Sudoku board (for instance, taking any Sudoku board from sudokus_start.txt), the program will generate a file called output.txt, containing a single line of text representing the finished Sudoku board. Since this board is solved, the string representation will contain no zeros. Here is an example of an output:
```483921657967345821251876493548132976729564138136798245372689514814253769695417382```
