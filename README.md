# Tic Tac Toe Game (Python)

## Overview

This project is a **two-player Tic Tac Toe game** implemented using **Python** and played in the **console**. The game uses a 3×3 matrix and allows two players to take turns marking positions with `X` and `O`.

The program validates user input, prevents overwriting already chosen positions, and checks all possible winning conditions after each move.

---

## Game Description

* The game board is represented using a 3×3 matrix.
* Positions are initially numbered from **1 to 9** for easy selection.
* Player 1 uses **X**.
* Player 2 uses **O**.
* Players alternate turns until one wins or the game ends.

---

## Rules of the Game

* Players choose a number between **1 and 9** corresponding to a board position.
* A position once selected cannot be reused.
* A player wins if they mark:

  * Any row
  * Any column
  * Either diagonal

---

## Technologies Used

* Python 3
* Lists (2D lists)
* Loops and conditional statements
* User input handling

---

## Project Structure

```
Tic-Tac-Toe/
│
├── tic_tac_toe.py   # Main game logic
├── README.md       # Project documentation
```

---

## How to Run the Game

### Prerequisites

* Python 3 installed on your system

### Run Command

```bash
python tic_tac_toe.py
```

---

## Code Logic Explanation

* A 2D list is used to represent the game board.
* A separate list stores already selected positions to prevent cheating.
* After every move, the program checks:

  * Diagonal match
  * Horizontal match
  * Vertical match
* The game stops immediately once a winning condition is met.

---

## Sample Output

```
1 2 3
4 5 6
7 8 9

ENTER:: 1
x 2 3
4 5 6
7 8 9

ENTER2:: 5
x 2 3
4 o 6
7 8 9
```

---

## Learning Outcomes

* Working with 2D lists
* Implementing turn-based logic
* Validating user input
* Applying conditional logic for win detection

---

## Future Improvements

* Draw condition handling
* Input validation for invalid numbers
* Single-player mode (vs computer)
* Refactoring code using functions
* GUI version using Tkinter

---

## Author

Gauri

---
