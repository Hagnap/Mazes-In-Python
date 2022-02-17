import random

def BinaryTreeMazeAlgorithm(maze):

    for i in range(len(maze)):
        for j in range(len(maze[i])):

            # Check if space can be traversed or not if maze[i][j].value != '0' → Traverse cell (Want to skip dead nodes)
            if maze[i][j].value != '0':
                continue

            # Helps us choose to add a wall to the North or East
            rand_direction = random.random()

            # North
            if rand_direction >= 0.5:
                rand_wall = random.random()

                # North
                if rand_wall >= 0.5:

                    ### Check above
                    if i == 0:
                        pass
                    else:
                        if maze[i - 1][j].value == '0':
                            maze[i - 1][j].value = '■'

            # East
            else:
                ### Check to the right
                if j == len(maze[i]) - 1:
                    pass
                else:
                    if maze[i][j + 1].value == '0':
                        maze[i][j + 1].value = '■'




    return maze
