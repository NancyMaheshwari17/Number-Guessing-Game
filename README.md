# Number Guessing Game (Python)

## Project Overview

This project is a **command-line Number Guessing Game built using Python**.
The computer randomly selects a number between **0 and 100**, and the player tries to guess it.

The program provides hints such as **"Too High" or "Too Low"** until the correct number is guessed.

The game also tracks **lowest attempts and highest attempts** using file handling.

## Features

* Random number generation
* Interactive user input
* Hint system (High / Low)
* Attempt counter
* Score tracking using file handling
* Saves **lowest and highest attempts**

## How the Game Works

1. The computer generates a random number between **0 and 100**.
2. The player enters a guess.
3. The program checks the guess and provides feedback:

   * Too high
   * Too low
4. The game continues until the correct number is guessed.
5. The program records:

   * Lowest attempts
   * Highest attempts

These statistics are stored in a file.

## Technologies Used

* Python
* Random module
* File handling

## Project Structure

number-guessing-game-python
│
├── project2.py
├── pro2_data.txt
└── README.md

## How to Run the Project

1. Install Python
2. Download or clone the repository
3. Run the program

python project2.py

4. Enter your guesses until you find the correct number.

## Example Output

Enter your guess (0-100): 40
It's Low!! Try again.

Enter your guess (0-100): 70
It's High!! Try again.

Enter your guess (0-100): 55
Correct! You guessed the number.

Lowest Attempts: 6
Highest Attempts: 9


