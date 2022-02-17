import random

def TestMazeAlgorithm(maze):

    for i in range(len(maze)):
        for j in range(len(maze[i])):

            # Check if space can be traversed or not if maze[i][j].value != '0' → Traverse cell
            if maze[i][j].value != '0':
                continue

            # Helps us choose to add a wall
            rand_wall = random.random()

            # Add wall to current cell
            if rand_wall >= 0.5:
                maze[i][j].value = '■'  # Alt Code: 254

            # Do nothing
            else:
                continue

    return maze
