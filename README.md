# 🕹️ Pygame Tic-Tac-Toe (AI vs. Player)

This repository holds a classic **Tic-Tac-Toe** game built with **Pygame** for Python. It features a powerful, unbeatable AI opponent that uses the **Minimax algorithm** to play optimally. You can run the game on your desktop or play it directly in a web browser, thanks to PyGbag!

| **🚀 Play the Game Live** |
| :--- |
| **URL:** `[https://mohammed-ba-qalaql.itch.io/tic-tac-toe-game-ai]`|

## 🌟 Features

* **Unbeatable AI:** The computer plays perfectly using the Minimax algorithm, ensuring the best possible outcome (win or draw) for the current AI player.
* **Player Selection:** Start the game by choosing to play as **X** (goes first) or **O** (goes second).
* **Web Compatibility:** Easily packaged for the web using **PyGbag**.
* **Simple Pygame Interface:** Clean, $600 \times 400$ graphical interface.

***

## ⚙️ Installation and Setup (Desktop)

### 1. Prerequisites

You must have **Python 3** installed.

### 2. Clone the Repository

```bash
git clone [https://github.com/mohammed-ba-qalaql/tic-tac-toe-AI.git]
cd [tic-tac-toe-AI]
````

### 3\. Install Dependencies

You only need the `pygame` library:

```bash
pip install pygame
```

### 4\. Run the Game

Execute the main script:

```bash
python main.py
```

-----

## 🧠 Core Game Logic (`tictactoe.py` content)

This module contains all the game rules and the AI's decision-making logic, including the Minimax implementation and its helper functions.

| Function | Description |
| :--- | :--- |
| `initial_state()` | Returns a standard, empty $3 \times 3$ board. |
| `player(board)` | Returns the player (`X` or `O`) whose turn is next. |
| `actions(board)` | Lists all currently **available** legal moves as $(row, col)$ tuples. |
| `result(board, action)` | Creates a **deep copy** of the board and applies the move, returning the new state. |
| `winner(board)` | Checks rows, columns, and diagonals, returning the winning player (`X` or `O`), or `None`. |
| `terminal(board)` | Checks if the game is over (a win for either side, or a full board draw). |
| `utility(board)` | Assigns a numerical value to a final state: **1** (X win), **-1** (O win), or **0** (tie). |
| `minimax(board)` | **The AI function.** Searches the game tree to find and return the move that guarantees the best score. |
| `maxValue(board)` | Helper function used by Minimax to find the best outcome for the **Maximizing Player (X)**. |
| `minValue(board)` | Helper function used by Minimax to find the best outcome for the **Minimizing Player (O)**. |

-----

## 🤝 Contribution

Feel free to **fork** the repository, submit pull requests, or open issues if you have suggestions or encounter bugs\!
