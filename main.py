from src.maze import Maze
from src.window import Window
from automated_crawler import AutomatedCrawler

def carve_path(maze, path):
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i + 1]

        if r1 == r2 and c1 + 1 == c2:
            maze.vertical_walls[r1][c1 + 1].toggle()
        elif r1 == r2 and c1 - 1 == c2:
            maze.vertical_walls[r1][c2 + 1].toggle()
        elif c1 == c2 and r1 + 1 == r2:
            maze.horizontal_walls[r1 + 1][c1].toggle()
        elif c1 == c2 and r1 - 1 == r2:
            maze.horizontal_walls[r2 + 1][c1].toggle()

def main():
    win = Window(800, 600)

    num_rows, num_cols = 6, 6
    cell_size_x, cell_size_y = 60, 60
    margin_x, margin_y = 50, 50

    maze = Maze(margin_x, margin_y, num_rows, num_cols, cell_size_x, cell_size_y, win)

    # define entrance and exit
    maze.mark_entrance(0, 0, side=1)  # top-left
    maze.mark_exit(num_rows-1, num_cols-1, side=3)  # bottom-right

    # carve a sample path
    path = [(0,0),(1,0),(2,0),(2,1),(2,2),(3,2),(4,2),(5,2),(5,3),(5,4),(5,5)]
    carve_path(maze, path)

    # redraw maze
    maze.redraw()

    # set neighbors (important for crawler movement)
    for r in range(num_rows):
        for c in range(num_cols):
            cell = maze.get_cell(r, c)
            if c > 0 and not cell.left_wall.exists: cell.left_cell = maze.get_cell(r, c-1)
            if c < num_cols-1 and not cell.right_wall.exists: cell.right_cell = maze.get_cell(r, c+1)
            if r > 0 and not cell.top_wall.exists: cell.top_cell = maze.get_cell(r-1, c)
            if r < num_rows-1 and not cell.bottom_wall.exists: cell.bottom_cell = maze.get_cell(r+1, c)

    # create automated crawler at entrance
    auto_crawler = AutomatedCrawler(maze.get_cell(0,0), win)
    auto_crawler.last_direction = "down"  # start pointing downward
    auto_crawler.draw()

    # run the automated crawler
    found = auto_crawler.run()

    print("Automated crawler reached the exit:", found)

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
