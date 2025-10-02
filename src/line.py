from tkinter import Canvas
from src.point import Point

class Line():
    def __init__(self, point1:Point, point2:Point, color = "black", width = 2):
        self.point1 = point1
        self.point2 = point2
        self.color = color
        self.width = width

    def draw(self, canvas:Canvas):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=self.color, width=self.width
        )