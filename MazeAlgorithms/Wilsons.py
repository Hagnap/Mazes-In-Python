import random
import numpy as np

import Utils

def WilsonsMazeAlgorithm(maze, mask, rows, cols):

    # Idea: Look for visited nodes, when one is found start at a random unvisited node
    unvisited = list()

    # Before creating the maze, add each node to the unvisited list
    for i in range(rows):
        for j in range(cols):
            unvisited.append(maze[i][j])

    # Mark Top-Left Corner if not masked)
    if mask[0][0] == 0:
        maze[0][0].value = '■'

    # Choose a random node to start at
    current = Utils.get_random_cell(maze, rows, cols)

    # Loop until each spot on the maze has been visited
    while len(unvisited) - np.count_nonzero(mask) > 0:

        # Check if we have been here before
        if Utils.is_node_in_list(unvisited, current):
            unvisited.remove(current)

            # Add wall or leave space open
            rand_wall = random.random()
            if rand_wall >= 0.625:

                if mask[current.row][current.col] == 0:
                    maze[current.row][current.col].value = '■'

        if len(unvisited) >= 1:
            # Select a random node to go to
            current = unvisited[np.random.randint(0, len(unvisited))]
        else:
            break

    return maze
