from src.maze import Maze
from src.window import Window
from src.player_crawler import PlayerCrawler



def main():
    win = Window(800, 600)

    num_rows, num_cols = 6, 6
    cell_size_x, cell_size_y = 60, 60
    margin_x, margin_y = 50, 50

    maze = Maze(margin_x, margin_y, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.mark_entrance(0, 0, side=1)
    maze.mark_exit(num_rows - 1, num_cols - 1, side=3)

    paths = [
        [(0,0),(1,0),(2,0),(3,0)],
        [(0,0),(0,1),(0,2),(0,3)],                      
        [(2,0),(2,1),(1,1)],
        [(2,2),(2,3),(1,3),(1,4),(1,5),(0,5)],    
        [(2,1),(2,2),(3,2),(4,2),(5,2),(5,3),(5,4),(5,5)]  
    ]

    for path in paths:
        maze.carve_path(path)

    maze.redraw()
    
    player = PlayerCrawler(maze.get_cell(0, 0), win, color="blue")
    player.last_direction = "down"
    player.draw()
    player.bind_keys()  # enable keyboard control

    win.wait_for_close()

if __name__ == "__main__":
    main()
