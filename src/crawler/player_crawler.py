from src.crawler.crawler import Crawler
from src.core.cell import Cell

import tkinter as tk
from tkinter import messagebox

class PlayerCrawler(Crawler):
    def __init__(self, start_cell, win, color="blue") -> None:
        super().__init__(start_cell, win)
        self.color = color

    def draw_move(self, from_cell:Cell, to_cell:Cell, undo=False) -> None:
        pass

    def bind_keys(self) -> None:
        canvas = self.win.get_canvas()
        canvas.focus_set()
        canvas.bind("<Up>", lambda e: self.try_move("up"))
        canvas.bind("<Down>", lambda e: self.try_move("down"))
        canvas.bind("<Left>", lambda e: self.try_move("left"))
        canvas.bind("<Right>", lambda e: self.try_move("right"))
        canvas.bind("<w>", lambda e: self.try_move("up"))
        canvas.bind("<s>", lambda e: self.try_move("down"))
        canvas.bind("<a>", lambda e: self.try_move("left"))
        canvas.bind("<d>", lambda e: self.try_move("right"))

    def try_move(self, direction:str) -> None:
        available = self.current_cell.get_available_directions()  
        print(f"try move {direction} ")
        for option in available:
            print(f'option:{option}')
        if direction in available:
            self.last_direction = direction
            super().move(direction)
            if self.current_cell.is_end:
                self._exit_maze(direction)
                messagebox.showinfo("Congratulations!", "You have reached the exit!")
        else:
            print('option not in direction')

    def _exit_maze(self, direction)-> None:
        super()._exit_maze(direction)

    def draw(self) -> None:
        if self.current_cell is None or self.win is None:
            return

        x, y = self.current_cell.center.x, self.current_cell.center.y
        size = 15
        width = size * 2 // 3

        if self.last_direction == "left":
            points = [x + size, y - width, x + size, y + width, x - size, y]
        elif self.last_direction == "right":
            points = [x - size, y - width, x - size, y + width, x + size, y]
        elif self.last_direction == "up":
            points = [x - width, y + size, x + width, y + size, x, y - size]
        elif self.last_direction == "down":
            points = [x - width, y - size, x + width, y - size, x, y + size]
        else:
            points = [x - width, y + size, x + width, y + size, x, y - size]

        if self.icon:
            self.win.get_canvas().delete(self.icon)
        self.icon = self.win.get_canvas().create_polygon(points, fill=self.color)
