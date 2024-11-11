# Sudoku Solver

This is a Python-based Sudoku solver that utilizes constraint propagation and backtracking to solve Sudoku puzzles. The solver can handle typical Sudoku puzzles, automatically deducing possible values for each cell and backtracking when necessary.

## Features

- **Constraint Propagation**: Automatically reduces possible values for each cell based on Sudoku rules.
- **Backtracking**: Ensures that even puzzles requiring guessing and checking can be solved.
- **Modular Design**: The solver functions are modular, making it easy to extend or modify.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/niki8885/sudoku.git
   ```
2. Navigate to the project directory:
   ```bash
   cd sudoku-solver/src
   ```
3. Ensure you have Python 3 installed. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install any dependencies (if required).

## Usage

1. **Run the solver**:
   The `main.py` file imports the `solve_sudoku` module and solves a sample Sudoku puzzle.

   ```bash
   python main.py
   ```

2. **Change the puzzle**:
   Update the `sudoku_puzzle` variable in `main.py` with your own puzzle. Use `0` for empty cells.

## File Structure

```
src/
├── main.py         # Entry point for the Sudoku solver
├── solve_sudoku.py # Contains all Sudoku solving logic
```

## How It Works

### Key Functions in `solve_sudoku.py`:

- `generate_options(board)`: Initializes possible values for empty cells.
- `fix_solo(board)`: Assigns a value to cells when only one possible value remains.
- `check_rows_columns(board)`: Eliminates options based on fixed values in the same row and column.
- `check_rects(board)`: Eliminates options based on fixed values in the same 3x3 sub-grid.
- `is_valid(board, row, col, num)`: Validates if a number can be placed in a specific cell.
- `solve_with_backtracking(board)`: Solves the puzzle using recursive backtracking.
- `solve(board)`: Orchestrates the solving process.

### Example Output:
```plaintext
[5, 3, 0, 0, 7, 0, 0, 0, 0]
[6, 0, 0, 1, 9, 5, 0, 0, 0]
[0, 9, 8, 0, 0, 0, 0, 6, 0]
[8, 0, 0, 0, 6, 0, 0, 0, 3]
[4, 0, 0, 8, 0, 3, 0, 0, 1]
[7, 0, 0, 0, 2, 0, 0, 0, 6]
[0, 6, 0, 0, 0, 0, 2, 8, 0]
[0, 0, 0, 4, 1, 9, 0, 0, 5]
[0, 0, 0, 0, 8, 0, 0, 7, 9]
-----------------------
[5, 3, 4, 6, 7, 8, 9, 1, 2]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
[1, 9, 8, 3, 4, 2, 5, 6, 7]
[8, 5, 9, 7, 6, 1, 4, 2, 3]
[4, 2, 6, 8, 5, 3, 7, 9, 1]
[7, 1, 3, 9, 2, 4, 8, 5, 6]
[9, 6, 1, 5, 3, 7, 2, 8, 4]
[2, 8, 7, 4, 1, 9, 6, 3, 5]
[3, 4, 5, 2, 8, 6, 1, 7, 9]
```

## Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.