Tetris in Python (Pygame)

This is a Tetris clone written in Python using the pygame library.

Overview

The game creates a classic Tetris experience with seven different tetromino shapes (S, Z, I, O, J, L, T). The pieces spawn at the top and fall down at a rate controlled by a fall_speed. As you clear rows, the game speeds up. Scoring follows the traditional Tetris scoring system for lines cleared (1 line = 40 points, 2 lines = 100 points, 3 lines = 300 points, 4 lines = 1200 points).

Features:
	•	Random Tetromino Generation: Each shape is randomly chosen for the next piece.
	•	Rotations & Movement: Control the current piece with arrow keys (left, right, up, down).
	•	Line Clearing: Full rows are cleared and score is updated accordingly.
	•	Speed Increase: The game gradually becomes faster over time.
	•	Game Over Detection: Game ends if new pieces cannot spawn without colliding.

Getting Started

Prerequisites
	•	Python 3 (3.6+ recommended)
	•	Pygame library

You can install Pygame via pip:

pip install pygame

How to Run
	1.	Clone or download this repository.
	2.	Open a terminal in the project directory.
	3.	Run the game:

python main.py


	4.	A window will open with the Tetris game.
	•	Press Any Key to start from the main menu.
	•	Control the falling piece using the arrow keys:
	•	Left/Right: Move horizontally
	•	Up: Rotate
	•	Down: Soft drop (faster fall)
	•	Close the window or press Esc (if you add an event handler for that) to exit.

Code Explanation
	•	Constants and Configuration
Several constants (colors, window dimensions, grid sizes) are defined at the start, making it easier to tweak the game’s appearance and mechanics.
	•	Piece Class
Encapsulates a single tetromino (shape). It stores the current position (x, y), the shape layout, color, and rotation state.
	•	Grid Creation & Rendering
	•	create_grid(locked_positions): Generates a 2D list that represents each cell of the play area.
	•	draw_grid(surface, grid): Draws the cells to the game window.
	•	Game Logic
	•	valid_space(piece, grid): Checks if the piece’s new position is valid (within boundaries and not overlapping locked blocks).
	•	clear_rows(grid, locked): Removes fully occupied rows and updates the locked positions.
	•	check_lost(positions): Checks if the game should end (blocks reaching the top).
	•	Main Loop
	•	In main(), the game runs a continuous loop, handling:
	1.	Timing: Controlling how fast pieces fall (fall_speed) and increasing speed periodically (level_time).
	2.	Input: Arrow keys to move or rotate the current piece.
	3.	Line Clearing: Adds scores and updates positions.
	4.	Game Over: If no space is available at the top for a new piece.
	•	Main Menu
	•	main_menu(): Displays a simple menu asking the user to press any key to start the game.

Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

Potential improvements:
	•	Add a hard drop functionality.
	•	Implement a pause feature.
	•	Add high score tracking.
	•	Enhance sound effects or graphics (e.g., better fonts, backgrounds).
