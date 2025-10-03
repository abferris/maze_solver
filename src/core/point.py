class Point():
    def __init__(self,x=int, y=int):
        self.x = x
        self.y = y
        self.position = {self.x,self.y}

    def get_position(self) -> tuple[int,int]:
        print(f"x:{self.x}, y:{self.y}")
        return self.position
    
    def move(self, x, y) -> tuple[int,int]:
        self.x += x
        self.y += y
        return self.get_position()
    