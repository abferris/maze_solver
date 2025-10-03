import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.maze import Maze


def carve_path(maze, path):
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i + 1]
        if r1 == r2 and c1 + 1 == c2:
            maze.vertical_walls[r1][c1 + 1].toggle()
        elif r1 == r2 and c1 - 1 == c2:
            maze.vertical_walls[r1][c2 + 1].toggle()
        elif c1 == c2 and r1 + 1 == r2:
            maze.horizontal_walls[r1 + 1][c1].toggle()
        elif c1 == c2 and r1 - 1 == r2:
            maze.horizontal_walls[r2 + 1][c1].toggle()

def setUp(self):
    self.num_rows = 4
    self.num_cols = 4
    self.cell_size = 10

class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    

    def check_entrance_exit_and_path(self, maze, entrance, exit_, path):
        maze.mark_entrance(*entrance)
        maze.mark_exit(*exit_)
        carve_path(maze, path)

        e_cell = maze.get_cell(*entrance[:2])
        x_cell = maze.get_cell(*exit_[:2])
        self.assertIsNotNone(e_cell)
        self.assertIsNotNone(x_cell)

        side = entrance[2] if len(entrance) > 2 else -1
        if side == 0:
            self.assertFalse(e_cell.left_wall.exists)
        elif side == 1:
            self.assertFalse(e_cell.top_wall.exists)
        elif side == 2:
            self.assertFalse(e_cell.right_wall.exists)
        elif side == 3:
            self.assertFalse(e_cell.bottom_wall.exists)

        side = exit_[2] if len(exit_) > 2 else -1
        if side == 0:
            self.assertFalse(x_cell.left_wall.exists)
        elif side == 1:
            self.assertFalse(x_cell.top_wall.exists)
        elif side == 2:
            self.assertFalse(x_cell.right_wall.exists)
        elif side == 3:
            self.assertFalse(x_cell.bottom_wall.exists)

        for i in range(len(path) - 1):
            r1, c1 = path[i]
            r2, c2 = path[i+1]
            if r1 == r2:
                idx = max(c1, c2)
                self.assertFalse(maze.vertical_walls[r1][idx].exists)
            elif c1 == c2:
                idx = max(r1, r2)
                self.assertFalse(maze.horizontal_walls[idx][c1].exists)

    def test_entrance_left_exit_right(self):
        maze = Maze(0, 0, self.num_rows, self.num_cols, self.cell_size, self.cell_size)
        self.check_entrance_exit_and_path(maze, (2,0,0), (2,3,2), [(2,0),(2,1),(2,2),(2,3)])

    def test_entrance_right_exit_top(self):
        maze = Maze(50, 0, self.num_rows, self.num_cols, self.cell_size, self.cell_size)
        self.check_entrance_exit_and_path(maze, (1,3,2), (0,0,1), [(1,3),(1,2),(1,1),(1,0),(0,0)])

    def test_entrance_top_exit_bottom(self):
        maze = Maze(0, 50, self.num_rows, self.num_cols, self.cell_size, self.cell_size)
        self.check_entrance_exit_and_path(maze, (0,1,1), (3,2,3), [(0,1),(1,1),(2,1),(3,1),(3,2)])

    def test_interior_entrance(self):
        maze = Maze(50, 50, self.num_rows, self.num_cols, self.cell_size, self.cell_size)
        self.check_entrance_exit_and_path(maze, (2,2), (1,1), [(2,2),(2,1),(1,1)])

    def test_interior_exit(self):
        maze = Maze(100, 0, self.num_rows, self.num_cols, self.cell_size, self.cell_size)
        self.check_entrance_exit_and_path(maze, (0,0), (3,3), [(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(3,3)])


if __name__ == "__main__":
    unittest.main()