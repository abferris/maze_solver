# maze_solver
**Author:** Aaron Ferris
**Github:** [github.com/abferris](https://github.com/abferris)
**Version:** 1.0
## Objective

The point is to practice python programming.

## Description

I wanted to do this based off the description of a  tutorial I saw from boot.dev. I saw some of the basics, but didn't like how it was handling how things were constructed or generated. I also wanted to make this into something that was interactive rather than just 'make a map

## Rules of the game

The crawler should be spawned at an entrance of a maze. You can see the auto crawler crawl the maze, or use the arrow key to crawl the maze itself.



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
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
├── src
│   ├── __init__.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── cell.py
│   │   ├── line.py
│   │   ├── point.py
│   │   └── wall.py
│   ├── crawler
│   │   ├── __init__.py
│   │   ├── auto_crawler.py
│   │   ├── crawler.py
│   │   └── player_crawler.py
│   ├── maze
│   │   ├── __init__.py
│   │   └── maze.py
│   └── ui
│       ├── __init__.py
│       └── window.py
└── tests
    ├── __init__.py
    └── tests.py
       

## Future Improvements

- option to generate of maze Randomly
- give a menu to select options

- option to run with auto_crawler
- option to run with player crawler
- option to create map
- option to exit application

- once inside run with
  - option to played randomly generated map or savep map
    - options for 4 different sizes
- is changing randomized map difficulty a thing
  - maybe changing the amount of active cells (cells with neighbors) in a maze
  - minimum amount of turns to get to exit
  - not sure how to achieve this
- after completion 
  - option to save map and name it before returning to main menu
  - reroute to main menu

- Ability to save maze
  - use a map object that doesn't have an edit option
- ability to create mazes
  - ability to clone existing maze and edit based off that
- ability to edit saved mazes
  - creation/editor should not have filled in cells