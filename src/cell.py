from src.window import Window
from src.line import Line
from src.point import Point
from src.wall import Wall

class Cell():
    def __init__(self, x1=-1, x2=-1, y1=-1, y2=-1, window:Window=None):
        self.left_wall: Wall = None
        self.right_wall: Wall = None
        self.top_wall: Wall = None
        self.bottom_wall: Wall = None

        self.left_cell: "Cell" = None
        self.right_cell: "Cell" = None
        self.top_cell: "Cell" = None
        self.bottom_cell: "Cell" = None

        self.is_start:bool = False
        self.is_end:bool = False
        self.exit_direction:int = -1


        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = window

    @property
    def center(self):
        return Point((self.__x1 + self.__x2)//2, (self.__y1 + self.__y2)//2)


    def draw(self):
        if self.__win is None:
            return
        x1 = self.__x1 
        x2 = self.__x2 
        y1 = self.__y1 
        y2 = self.__y2

        color = "black" if self.has_left_wall else "white"
        left_line = Line(Point(x1,y1), Point(x1,y2),color)
        self.__win.draw_line(left_line)
        
        color = "black" if self.has_top_wall else "white"
        left_line = Line(Point(x1,y1), Point(x2,y1),color)
        self.__win.draw_line(left_line)
        
        color = "black" if self.has_right_wall else "white"
        left_line = Line(Point(x2,y1), Point(x2,y2),color)
        self.__win.draw_line(left_line)
        
        color = "black" if self.has_bottom_wall else "white"
        left_line = Line(Point(x1,y2), Point(x2,y2),color)
        self.__win.draw_line(left_line)


    def draw_move(self, to_cell:"Cell", undo=False):
        if self.__win is None:
            return
        x_center = (self.__x2 + self.__x1)//2
        y_center = (self.__y2 + self.__y1)//2

        x_center2 = (to_cell.__x2 + to_cell.__x1)//2
        y_center2 = (to_cell.__y2 + to_cell.__y1)//2
   
        color = "red" if not undo else "gray"

        move_line = Line(Point(x_center, y_center), Point(x_center2, y_center2), color=color, width=2)
        self.__win.draw_line(move_line)

    def clear(self):
        if self.__win is None:
            return
        padding = 2
        self.__win._Window__canvas.create_rectangle(
            self.__x1 + padding, self.__y1 + padding,
            self.__x2 - padding, self.__y2 - padding,
            fill="white", outline=""
        )

    def set_neighbors(self):
        for r in range(self.__num_rows):
            for c in range(self.__num_cols):
                cell = self.__cells[c][r]

                # left neighbor
                if c > 0 and not cell.left_wall.exists:
                    cell.left_cell = self.__cells[c - 1][r]

                # right neighbor
                if c < self.__num_cols - 1 and not cell.right_wall.exists:
                    cell.right_cell = self.__cells[c + 1][r]

                # top neighbor
                if r > 0 and not cell.top_wall.exists:
                    cell.top_cell = self.__cells[c][r - 1]

                # bottom neighbor
                if r < self.__num_rows - 1 and not cell.bottom_wall.exists:
                    cell.bottom_cell = self.__cells[c][r + 1]
