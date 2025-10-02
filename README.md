# maze_solver
**Author:** Aaron Ferris
**Github:** [github.com/abferris](https://github.com/abferris)
**Version:** 1.0
## Objective

The point is to practice python programming.

## Rules of the game

The point of this is to make a bot that can solve a maze


## Pre-Requirement Installs

- python 
  - https://www.python.org/downloads/
- pip installer
  - https://pip.pypa.io/en/stable/installation/
- tk
    - sudo apt-get install python3-tk



## Running Instructions

Assuming you have python and pip
Commands to run to get this to work:
- git clone https://github.com/abferris/maze_solver maze_solver
- cd maze_solver
- sudo apt-get install python3-tk
- python3 main.py

## Folder Structure

maze_solver/
├── main.py
├── pyproject.toml
├── README.md
├── .gitignore
└── src/
    ├── core
    │   ├── constants.py   # game constants which can be changed to mod the game
    highscore.py
    ├── data/
    │   └── highscores.json # this is ignored and will be created when you first run the game
    ├── game/
    │   ├── __init__.py
    │   ├── background.py  
    │   ├── circleshape.py
    │   ├── enemies/
    │   │   ├── __init__.py
    │   │   ├── asteroid.py
    │   │   └── asteroidfield.py
    │   └── player/
    │      ├── __init__.py
    │      ├── player.py
    │      └── shot.py
    └── ui/
        ├── __init__.py   
        ├── menu_helpers.py
        ├── menu_inputs.py
        ├── menu.py
        └── score.hud.py
       

## Future Improvements
- add typing to everything
- fix the 5 looking weird when printing
- add the ability to use assets
  - potential to add background asset
  - replace triangle with a ship image
  - be able to replace asteroid circles with assets
    - potential for multiple asteroid assets
  - change the shot
    - make the shot color change
    - add a small explosion for shots connecting
- make an option for playing with lives
  - potentially gain a life after a certain amount of points
- make the singular highscore into a leaderboard
- allow for initials to be inserted with a high score
- powerups/debuffs
  - shot mods
    - multiple 
    - shot speed up
    - homing
    - explosive shot
  - ship mods
    - shield
    - accelleration
- allow for fullscreen mode/screen size changes
  - set up minimum screen size
- secondary menu to modify constants in game
  - if constants are modified, high score is reset
  - warning that doing this will reset your high score
  - option to reset high score by itself
- setup safegaurd of high scores being tampered with manually
- setting up so this game can run without terminal from an icon
- adding enemies

- not sure if i should be adding output typing to all of my fuctions. 
  - Not sure where it is appropriate
  - need feedback on where function inputs and outputs need typing

## Screen Shots
Fig. 1: Home Screen

<img width="1286" height="748" alt="Screenshot 2025-08-30 014732" src="https://github.com/user-attachments/assets/9a1435cb-703f-43a8-84ec-3727b0c57326" />

Fig. 2: Gameplay

<img width="1287" height="750" alt="Screenshot 2025-08-30 014656" src="https://github.com/user-attachments/assets/c96220e7-1ecf-4750-95b7-a2a0790befa8" />

Fig. 3: Pause Screen

<img width="1287" height="749" alt="Screenshot 2025-08-30 014748" src="https://github.com/user-attachments/assets/7fc6bbbe-8726-450a-b8ee-861f169f4105" />

Fig. 4: Game Over menu

<img width="1289" height="750" alt="Screenshot 2025-08-30 014708" src="https://github.com/user-attachments/assets/1060a2a0-a4c2-4722-8d43-e551b0608dc0" />

