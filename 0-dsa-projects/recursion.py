def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)



'''→ 4 + sum_to_n(3)
→ 4 + (3 + sum_to_n(2))
→ 4 + (3 + (2 + sum_to_n(1)))
→ 4 + (3 + (2 + 1)'''



# Mazesolver 

def maze_solver(maze, x, y, goal):
    rows = len(maze)
    cols = len(maze[0])

    # Base cases
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return False  # out of bounds
    
    if maze[x][y] != 0:
        return False  # wall or already visited

    if (x, y) == goal:
        return True  # reached goal

    # Mark as visited
    maze[x][y] = 2  # 2 = visited

    # Explore all 4 directions
    if (maze_solver(maze, x + 1, y, goal) or  # down
        maze_solver(maze, x - 1, y, goal) or  # up
        maze_solver(maze, x, y + 1, goal) or  # right
        maze_solver(maze, x, y - 1, goal)):   # left
        return True

    # Backtrack
    maze[x][y] = 0
    return False


maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]

start = (0, 0)
goal = (3, 3)

result = maze_solver(maze, start[0], start[1], goal)
print(result)  # True or False




