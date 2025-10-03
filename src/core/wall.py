from tkinter import Canvas
from src.core.point import Point
from src.core.line import Line

class Wall():
    def __init__(self, point1:Point, point2:Point, window=None):
        self.point1 = point1
        self.point2 = point2
        self.width = 2
        self.exists = True
        self.__win = window
    
    @property
    def color(self):
        return "black" if self.exists else "white"
    
    @property
    def line(self):
        return Line(self.point1,self.point2, color=self.color, width=2)
    
    def draw(self):
        if self.__win is None:
            return
        canvas = self.__win.get_canvas()
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=self.color, width=self.width
        )

    def toggle(self):
        self.exists = not self.exists
        canvas = self.__win.get_canvas()
        self.line.draw(canvas)