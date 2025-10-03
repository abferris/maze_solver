from tkinter import Tk, BOTH, Canvas
from src.core.line import Line

class Window ():
    def __init__(self, width:int, height:int, bg_color:str="white", title:str = "Maze Solver"):
        
        self.__root = Tk()
        self.__root.title = title
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg=bg_color, height=height, width=width)
        self.__canvas.pack(fill="both", expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("closing")


    def get_canvas(self):
        return self.__canvas
    
    def draw_line(self,line:Line):
        line.draw(self.__canvas)

    def close(self):
        self.__running = False
        self.__root.protocol()