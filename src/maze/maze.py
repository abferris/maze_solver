import time
import random
from typing import Dict


from src.core.cell import Cell
from src.core.line import Line
from src.ui.window import Window
from src.core.point import Point
from src.core.wall import  Wall

class Maze():
    def __init__(self, x1:int, y1:int, num_rows:int, num_cols:int,
                 cell_size_x:int, cell_size_y:int, win:Window=None, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.vertical_walls = self.vertical_walls = [[None]*(num_cols+1) for _ in range(num_rows)]
        self.horizontal_walls = [[None]*num_cols for _ in range(num_rows+1)]  

        self.__cells = [[None]*num_cols for _ in range(num_rows)]

        if seed is not None:
            random.seed(seed)


        self.entrance = None
        self.exit = None


        self.__create_walls()
        self.__create_cells()

    def get_cell(self, i, j) -> Cell:
        return self.__cells[i][j]
    
    def __create_walls(self) -> None:
        for r in range(self.__num_rows):
            for c in range(self.__num_cols+1):
                x = self.__x1 + c * self.__cell_size_x
                y1 = self.__y1 + r * self.__cell_size_y
                y2 = y1 + self.__cell_size_y
                self.vertical_walls[r][c] = Wall(Point(x, y1), Point(x, y2), self.__win)

        for r in range(self.__num_rows+1):
            for c in range(self.__num_cols):
                x1 = self.__x1 + c * self.__cell_size_x
                x2 = x1 + self.__cell_size_x
                y = self.__y1 + r * self.__cell_size_y
                self.horizontal_walls[r][c] = Wall(Point(x1, y), Point(x2, y), self.__win)

    def __create_cells(self) -> None:
        for r in range(self.__num_rows):
            for c in range(self.__num_cols):
                x1 = self.__x1 + c * self.__cell_size_x
                y1 = self.__y1 + r * self.__cell_size_y
                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y
                cell = Cell(x1, x2, y1, y2, self.__win)

                # assign shared walls
                cell.left_wall = self.vertical_walls[r][c]
                cell.right_wall = self.vertical_walls[r][c+1]
                cell.top_wall = self.horizontal_walls[r][c]
                cell.bottom_wall = self.horizontal_walls[r+1][c]

                self.__cells[r][c] = cell


    def __make_edge_opening(self, cell:Cell, side:int) -> Cell:
        if side == 0 and cell.left_wall and cell.left_wall.exists:
            cell.left_wall.toggle()
        elif side == 1 and cell.top_wall and cell.top_wall.exists:
            cell.top_wall.toggle()
        elif side == 2 and cell.right_wall and cell.right_wall.exists:
            cell.right_wall.toggle()
        elif side == 3 and cell.bottom_wall and cell.bottom_wall.exists:
            cell.bottom_wall.toggle()
        return cell

    def mark_entrance(self, row:int, col:int, side:int=None) -> None:
        self.entrance = (row, col, side)
        cell = self.get_cell(row, col)
        cell.is_start = True

        if side is None:
            if col == 0: side = 0
            elif col == self.__num_cols-1: side = 2
            elif row == 0: side = 1
            elif row == self.__num_rows-1: side = 3
            else: side = -1

        if side in (0,1,2,3):
            self.__make_edge_opening(cell, side)

        if self.__win is None:
            return

        x_center, y_center = cell.center.x, cell.center.y
        offset = 20

        if side == 0:
            start = Point(cell.left_wall.point1.x - offset, y_center)
            end = cell.center
            self.__win.draw_line(Line(start, end, color="blue", width=3, arrow="last"))
        elif side == 1:
            start = Point(x_center, cell.top_wall.point1.y - offset)
            end = cell.center
            self.__win.draw_line(Line(start, end, color="blue", width=3, arrow="last"))
        elif side == 2:
            start = Point(cell.right_wall.point1.x + offset, y_center)
            end = cell.center
            self.__win.draw_line(Line(start, end, color="blue", width=3, arrow="last"))
        elif side == 3:
            start = Point(x_center, cell.bottom_wall.point1.y + offset)
            end = cell.center
            self.__win.draw_line(Line(start, end, color="blue", width=3, arrow="last"))
        else:
            canvas = self.__win.get_canvas()
            canvas.create_text(x_center, y_center, text="E", fill="blue", font=("Arial",16,"bold"))

    def mark_exit(self, row:int, col:int, side:int=None) -> None:
        cell = self.get_cell(row, col)
        self.exit = (row, col, side)
        cell.is_end = True
        cell.exit_direction = side

        if side is None:
            if col == 0: side = 0
            elif col == self.__num_cols-1: side = 2
            elif row == 0: side = 1
            elif row == self.__num_rows-1: side = 3
            else: side = -1

        if side in (0,1,2,3):
            self.__make_edge_opening(cell, side)

        if self.__win is None:
            return

        x_center, y_center = cell.center.x, cell.center.y
        offset = 20

        if side == 0:
            start = Point(cell.left_wall.point1.x - offset, y_center)
            end = cell.center
        elif side == 1:
            start = Point(x_center, cell.top_wall.point1.y - offset)
            end = cell.center
        elif side == 2:
            start = Point(cell.right_wall.point1.x + offset, y_center)
            end = cell.center
        elif side == 3:
            start = Point(x_center, cell.bottom_wall.point1.y + offset)
            end = cell.center
        else:
            canvas = self.__win.get_canvas()
            canvas.create_text(x_center, y_center, text="X", fill="green", font=("Arial",16,"bold"))
            return

        if start and end:
            self.__win.draw_line(Line(start, end, color="green", width=3, arrow="first"))

    def redraw(self) -> None:
        for row_walls in self.vertical_walls:
            for wall in row_walls:
                wall.draw()
        for row_walls in self.horizontal_walls:
            for wall in row_walls:
                wall.draw()
        for row_cells in self.__cells:
            for cell in row_cells:
                cell.draw()

        if self.entrance: self.mark_entrance(*self.entrance)
        if self.exit: self.mark_exit(*self.exit)

        self.__win.redraw()

    def get_available_directions(self, cell:Cell)-> Dict[str,Cell]:
        directions = {}
        if cell.left_wall is None or not cell.left_wall.exists:
            if col > 0:
                directions["left"] = self.__cells[col-1][row]

        if cell.right_wall is None or not cell.right_wall.exists:
            if col < self.__num_cols - 1:
                directions["right"] = self.__cells[col+1][row]

        if cell.top_wall is None or not cell.top_wall.exists:
            if row > 0:
                directions["up"] = self.__cells[col][row-1]

        if cell.bottom_wall is None or not cell.bottom_wall.exists:
            if row < self.__num_rows - 1:
                directions["down"] = self.__cells[col][row+1]

        return directions
    
    def set_all_neighbors(self) -> None:
        for r in range(self.__num_rows):
            for c in range(self.__num_cols):
                cell = self.__cells[r][c]
                if cell.left_wall is None or not cell.left_wall.exists:
                    if c > 0:
                        cell.left_cell = self.__cells[r][c-1]
                if cell.right_wall is None or not cell.right_wall.exists:
                    if c < self.__num_cols - 1:
                        cell.right_cell = self.__cells[r][c+1]
                if cell.top_wall is None or not cell.top_wall.exists:
                    if r > 0:
                        cell.top_cell = self.__cells[r-1][c]
                if cell.bottom_wall is None or not cell.bottom_wall.exists:
                    if r < self.__num_rows - 1:
                        cell.bottom_cell = self.__cells[r+1][c]

    def carve_path(self, path:list[tuple[int,int]]) -> None:
        for i in range(len(path) - 1):
            r1, c1 = path[i]
            r2, c2 = path[i + 1]

            if r1 == r2 and c1 + 1 == c2:
                self.vertical_walls[r1][c1 + 1].toggle()
            elif r1 == r2 and c1 - 1 == c2:
                self.vertical_walls[r1][c2 + 1].toggle()
            elif c1 == c2 and r1 + 1 == r2:
                self.horizontal_walls[r1 + 1][c1].toggle()
            elif c1 == c2 and r1 - 1 == r2:
                self.horizontal_walls[r2 + 1][c1].toggle()
                
        self.set_all_neighbors()
        self.redraw()
