from collections import deque

class MazeSolver:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        
    def solve_maze(self, maze, start, end):
        queue = deque([start])
        visited = set([start])
        parent = {}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            current = queue.popleft()
            if current == end:
                path = []
                while current in parent:
                    path.append(current)
                    current = parent[current]
                path.append(start)
                return path[::-1]

            for dx, dy in directions:
                next_x, next_y = current[0] + dx, current[1] + dy
                if (0 <= next_x < self.cols and 0 <= next_y < self.rows and 
                    (next_x, next_y) not in visited and maze[next_y][next_x] == 0):
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))
                    parent[(next_x, next_y)] = current

        return []