import pygame
from maze_generator import MazeGenerator 
from maze_solver import MazeSolver
from maze_gui import MazeGUI

def main():
    # Constants
    WIDTH, HEIGHT = 1000, 700
    CELL_SIZE = 20
    ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
    
    # Initialize components
    generator = MazeGenerator(COLS, ROWS)
    solver = MazeSolver(COLS, ROWS)
    gui = MazeGUI(WIDTH, HEIGHT, CELL_SIZE)
    
    # Generate and solve maze
    maze, start, end = generator.generate_maze()
    path = solver.solve_maze(maze, start, end)
    
    # Main game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        gui.screen.fill(gui.WHITE)
        gui.draw_incremental_path(path, maze, start, end)
        clock.tick(300)

if __name__ == "__main__":
    main()