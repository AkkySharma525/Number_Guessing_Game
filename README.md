# Number Guessing Game

This is a simple Python-based number guessing game where the player has to guess a target number within a certain number of attempts. The game offers three difficulty levels and gives the user a fixed number of chances to guess the number. 

## Features

- **Difficulty Levels**: 
  - **Easy (E)**: Target number is randomly chosen between 1 and 20.
  - **Medium (M)**: Target number is randomly chosen between 1 and 40.
  - **Hard (H)**: Target number is randomly chosen between 1 and 60.
  
- **Fixed Number of Chances**: The user has 5 chances to guess the target number.

- **Interactive Feedback**: The game gives feedback after each guess, indicating whether the guess is too high or too low and how many chances are left.

- **Game Outcome**: 
  - If the user guesses correctly within the allowed chances, they win.
  - If the user runs out of chances without guessing correctly, they lose, and the correct number is revealed.

## How to Play

1. **Choose Difficulty Level**: 
   - Type `E` for Easy
   - Type `M` for Medium
   - Type `H` for Hard
   
2. **Guess the Target Number**: After choosing the difficulty level, you will be prompted to guess the target number. Enter a number or type `0` to quit the game.

3. **Game Feedback**: 
   - If your guess is too small, the game will ask you to guess a larger number.
   - If your guess is too large, the game will ask you to guess a smaller number.
   - The game will tell you how many chances are left after each guess.

4. **Game End**: The game ends when you either guess the target number correctly or run out of chances.

## Example of Gameplay

Choose Difficulty LEVEL(E,M,H): E Guess the target OR select 0 for quit= 10 You selected smaller no... Guess bigger no. TRY AGAIN! 4 chances left
Guess the target OR select 0 for quit= 15 You selected smaller no... Guess bigger no. TRY AGAIN! 3 chances left
Guess the target OR select 0 for quit= 18 You selected smaller no... Guess bigger no. TRY AGAIN! 2 chances left
Guess the target OR select 0 for quit= 19 YOU WON!! Congratulations ---GAME OVER---


## Code Explanation

1. **Difficulty Level Selection**:
   - The user is prompted to select a difficulty level (`E`, `M`, `H`). Based on the choice, a random target number is generated within the appropriate range.
   
2. **Guessing Loop**:
   - The player has 5 chances to guess the target number. If the guess is correct, the player wins and the game ends. If the guess is incorrect, the game provides feedback whether the number should be higher or lower and displays how many chances are left.

3. **Game End**:
   - If the player runs out of chances without guessing the correct number, the game ends and the correct number is revealed.

## Requirements

- **Python**: This game is written in Python, and you need Python 3.x installed on your machine to run it.

## How to Run the Game

1. Download or clone this repository.
2. Open a terminal or command prompt.
3. Navigate to the directory where the game script is saved.
4. Run the script using Python:
   ```bash
   python guessing_game.py

## Customization

You can change the number of attempts or modify the difficulty levels by adjusting the target range and number of chances in the code.
