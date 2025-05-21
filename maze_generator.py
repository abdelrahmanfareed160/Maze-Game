import random

class MazeGenerator:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        
    def generate_maze(self):
        maze = [[1 for _ in range(self.cols)] for _ in range(self.rows)]
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        stack = []

        start_x, start_y = random.randint(0, self.cols - 1), random.randint(0, self.rows - 1)
        end_x, end_y = random.randint(0, self.cols - 1), random.randint(0, self.rows - 1)

        stack.append((start_x, start_y))
        visited[start_y][start_x] = True
        maze[start_y][start_x] = 0

        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]

        while stack:
            current_x, current_y = stack[-1]
            unvisited_neighbors = []

            for dx, dy in directions:
                nx, ny = current_x + dx, current_y + dy
                if 0 <= nx < self.cols and 0 <= ny < self.rows and not visited[ny][nx]:
                    unvisited_neighbors.append((nx, ny))

            if unvisited_neighbors:
                next_x, next_y = random.choice(unvisited_neighbors)
                stack.append((next_x, next_y))
                visited[next_y][next_x] = True
                maze[next_y][next_x] = 0

                wall_x, wall_y = (current_x + next_x) // 2, (current_y + next_y) // 2
                maze[wall_y][wall_x] = 0
            else:
                stack.pop()

        maze[end_y][end_x] = 0
        return maze, (start_x, start_y), (end_x, end_y)