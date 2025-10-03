from src.crawler.crawler import Crawler
from src.core.cell import Cell
import time

class AutomatedCrawler(Crawler):
    def __init__(self, start_cell:Cell, win):
        super().__init__(start_cell, win)
        self.visited = set() 
        self.path = []

    def run(self) -> bool:
        return self._explore(self.current_cell)

    def _explore(self, cell:Cell) -> bool:
        self.visited.add(cell)
        self.path.append(cell)

        directions = self.get_directions()
        for d in directions:
            next_cell = self._get_neighbor(cell, d)
            if next_cell and next_cell not in self.visited:
                self.last_direction = d
                self.move(d)
                if next_cell.is_end:
                    return True
                if self._explore(next_cell):
                    return True
                self.last_direction = self._opposite_direction(d)
                self.move(self._opposite_direction(d), undo=True)

        self.path.pop()
        return False

    def _get_neighbor(self, cell:Cell, direction:str) -> Cell:
        if direction == "left": return cell.left_cell
        if direction == "right": return cell.right_cell
        if direction == "up": return cell.top_cell
        if direction == "down": return cell.bottom_cell
        return None

    def _opposite_direction(self, direction:str) -> str:
        return {"left": "right", "right": "left", "up": "down", "down": "up"}[direction]
