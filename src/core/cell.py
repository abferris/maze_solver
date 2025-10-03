from src.ui.window import Window
from src.core.line import Line
from src.core.point import Point
from src.core.wall import Wall

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
    def fill(self) -> str:
        if self.left_wall is None or not self.left_wall.exists or self.right_wall is None or not self.right_wall.exists or self.top_wall is None or not self.top_wall.exists or self.bottom_wall is None or not self.bottom_wall.exists:
            return 'white'
        return 'black'

    @property
    def center(self) -> Point:
        return Point((self.__x1 + self.__x2)//2, (self.__y1 + self.__y2)//2)


    def draw(self) -> None:
        if self.__win is None:
            return
        x1 = self.__x1 
        x2 = self.__x2 
        y1 = self.__y1 
        y2 = self.__y2

        canvas = self.__win.get_canvas()
        canvas.create_rectangle(x1, y1, x2, y2, fill=self.fill, outline='')
        print(self.fill)


        color = "black" if self.left_wall and self.left_wall.exists else "white"
        left_line = Line(Point(x1,y1), Point(x1,y2),color)
        self.__win.draw_line(left_line)
        
        color = "black" if self.top_wall and self.top_wall.exists else "white"
        left_line = Line(Point(x1,y1), Point(x2,y1),color)
        self.__win.draw_line(left_line)
        
        color = "black" if self.right_wall and self.right_wall.exists else "white"
        left_line = Line(Point(x2,y1), Point(x2,y2),color)
        self.__win.draw_line(left_line)
        
        color = "black" if self.bottom_wall and self.bottom_wall.exists else "white"
        left_line = Line(Point(x1,y2), Point(x2,y2),color)
        self.__win.draw_line(left_line)


    def draw_move(self, to_cell:"Cell", undo:bool=False) -> None:
        if self.__win is None:
            return
        x_center = (self.__x2 + self.__x1)//2
        y_center = (self.__y2 + self.__y1)//2

        x_center2 = (to_cell.__x2 + to_cell.__x1)//2
        y_center2 = (to_cell.__y2 + to_cell.__y1)//2
   
        color = "red" if not undo else "gray"

        move_line = Line(Point(x_center, y_center), Point(x_center2, y_center2), color=color, width=2)
        self.__win.draw_line(move_line)

    def clear(self) -> None:
        if self.__win is None:
            return
        padding = 2
        self.__win._Window__canvas.create_rectangle(
            self.__x1 + padding, self.__y1 + padding,
            self.__x2 - padding, self.__y2 - padding,
            fill=self.fill, outline=""
        )

    def set_neighbors(self) -> None:
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

    def get_available_directions(self) -> list:
        directions = []
        if self.left_wall is None or not self.left_wall.exists:
            print(self.left_cell)
            if self.left_cell:
               directions.append("left")
        print(self.right_wall is None or not self.right_wall.exists)
        if self.right_wall is None or not self.right_wall.exists:
            print(self.right_cell)
            if self.right_cell:
               directions.append("right")
        if self.top_wall is None or not self.top_wall.exists:
            if self.top_cell:
               directions.append("up")
        if self.bottom_wall is None or not self.bottom_wall.exists:
            if self.bottom_cell:
               directions.append("down")


        return directions