import pygame

class MazeGUI:
    WHITE = (255, 255, 255)
    BLACK = "#545454"
    RED = "#5cd89f"
    BLUE = "#ff5c3e"
    
    def __init__(self, width, height, cell_size):
        pygame.init()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Maze Generator")
        
    def draw_incremental_path(self, path, maze, start, end):
        for i, (x, y) in enumerate(path):
            for row in range(len(maze)):
                for col in range(len(maze[0])):
                    color = self.WHITE if maze[row][col] == 0 else self.BLACK
                    pygame.draw.rect(self.screen, color, 
                                  (col * self.cell_size, row * self.cell_size, 
                                   self.cell_size, self.cell_size))

            pygame.draw.rect(self.screen, self.RED, 
                           (start[0] * self.cell_size, start[1] * self.cell_size, 
                            self.cell_size, self.cell_size))
            pygame.draw.rect(self.screen, self.RED, 
                           (end[0] * self.cell_size, end[1] * self.cell_size, 
                            self.cell_size, self.cell_size))

            for j in range(i + 1):
                px, py = path[j]
                pygame.draw.rect(self.screen, self.BLUE, 
                               (px * self.cell_size, py * self.cell_size, 
                                self.cell_size, self.cell_size))

            pygame.display.flip()
            pygame.time.delay(15)
