import random

def SidewinderMazeAlgorithm(maze):

    for i in range(len(maze)):
        for j in range(len(maze[i])):

            # Helps us choose to add a wall to the East
            rand_direction = random.random()

            # Add wall to the East
            if rand_direction >= 0.5:
                ### Check Right
                if j == len(maze[i]) - 1:
                    pass
                else:
                    if maze[i][j + 1].value == '0':
                        maze[i][j + 1].value = '■'

            # Add wall to current cell
            else:
                rand_wall = random.random()

                # Does a wall get added to the current cell?
                if rand_wall >= 0.75:
                    if maze[i][j].value == '0':
                        maze[i][j].value = '■'

    return maze
