from src.line import Line
from src.point import Point
import time

class Crawler:
    def __init__(self, start_cell, win):
        self.current_cell = start_cell
        self.win = win
        self.icon = None
        self.last_direction = None  # orientation

    def draw(self):
        if self.current_cell is None or self.win is None:
            return

        x, y = self.current_cell.center.x, self.current_cell.center.y
        size = 15
        width = size * 2 // 3

        # Triangle points based on last_direction
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
        self.icon = self.win.get_canvas().create_polygon(points, fill="red")

    def get_directions(self):
        directions = []
        if self.current_cell.left_cell: directions.append("left")
        if self.current_cell.right_cell: directions.append("right")
        if self.current_cell.top_cell: directions.append("up")
        if self.current_cell.bottom_cell: directions.append("down")
        return directions

    def draw_move(self, from_cell, to_cell, undo=False):
        if self.win is None:
            return

        x1, y1 = from_cell.center.x, from_cell.center.y
        x2, y2 = to_cell.center.x, to_cell.center.y

        color = "red" if not undo else "gray"
        move_line = Line(Point(x1, y1), Point(x2, y2), color=color, width=2)
        self.win.draw_line(move_line)

    def move(self, direction,undo=False):
        next_cell = None
        if direction == "left": next_cell = self.current_cell.left_cell
        elif direction == "right": next_cell = self.current_cell.right_cell
        elif direction == "up": next_cell = self.current_cell.top_cell
        elif direction == "down": next_cell = self.current_cell.bottom_cell

        if not next_cell:
            return False

        self.draw_move(self.current_cell, next_cell, undo=undo)
        self.current_cell = next_cell
        self.last_direction = direction
        self.draw()
        self.win.get_canvas().update()
        time.sleep(0.3)
        if self.at_exit():
            self._exit_maze(direction)

    def at_exit(self):
        return self.current_cell.is_end if self.current_cell else False
    
    def _exit_maze(self, _):

        direction = None
        if not self.current_cell.top_wall.exists and self.current_cell.top_cell is None:
            direction = "up"
        elif not self.current_cell.bottom_wall.exists and self.current_cell.bottom_cell is None:
            direction = "down"
        elif not self.current_cell.left_wall.exists and self.current_cell.left_cell is None:
            direction = "left"
        elif not self.current_cell.right_wall.exists and self.current_cell.right_cell is None:
            direction = "right"
        
        if direction:
            self.last_direction = direction
            x, y = self.current_cell.center.x, self.current_cell.center.y

            step_size = 5
            steps = 20

            for _ in range(steps):
                if direction == "left":
                    x -= step_size
                elif direction == "right":
                    x += step_size
                elif direction == "up":
                    y -= step_size
                elif direction == "down":
                    y += step_size

                if self.icon:
                    self.win.get_canvas().delete(self.icon)

                self.icon = self.__draw_at(x, y, direction)
                self.win.get_canvas().update()
                time.sleep(0.05)

    def __draw_at(self, x, y, direction):
        size = 15
        width = size * 2 // 3

        if direction == "left":
            points = [x + size, y - width, x + size, y + width, x - size, y]
        elif direction == "right":
            points = [x - size, y - width, x - size, y + width, x + size, y]
        elif direction == "up":
            points = [x - width, y + size, x + width, y + size, x, y - size]
        elif direction == "down":
            points = [x - width, y - size, x + width, y - size, x, y + size]
        else:
            points = [x - width, y + size, x + width, y + size, x, y - size]

        return self.win.get_canvas().create_polygon(points, fill="red")

