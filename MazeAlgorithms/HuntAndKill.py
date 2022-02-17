import numpy as np
import random

import Utils

def HuntAndKillMazeAlgorithm(maze, mask, rows, cols):

    # Idea: Look for visited nodes, when one is found start at a random unvisited node
    visited = list()
    unvisited = list()

    # Choose a random node to start at
    current = Utils.get_random_cell(maze, rows, cols)

    # Before creating the maze, add each node to the unvisited list
    for i in range(rows):
        for j in range(cols):
            unvisited.append(maze[i][j])
    print(len(unvisited))
    count = 0

    while len(unvisited) - np.count_nonzero(mask) + 1 > 0:

        count += 1
        print(f'Iteration #{count}')

        if Utils.is_node_in_list(unvisited, current):
            unvisited.remove(current)
            visited.append(current)

            # Randomly at a wall
            rand_wall = random.random()
            if rand_wall >= 0.625:
                if mask is not None:
                    if mask[current.row][current.col] == 0:
                        maze[current.row][current.col].value = '■'
                else:
                    maze[current.row][current.col].value = '■'

        else:

            # Get neighbors
            neighbors = Utils.get_neighbors(current)


            # Choose a random neighbor
            #current = neighbors[np.random.randint(0, len(neighbors))]

            # Select a neighbor at random (Faces similar issue as the AldousBroderMazeAlgorithm)
            if len(neighbors) > 0:
                rand_neighbor = np.random.randint(0, len(neighbors))
                print(f'{rand_neighbor} -- Out of Indices: {len(neighbors) - 1} ({len(neighbors)})')
                current = neighbors[rand_neighbor]

            # If there is no neighbor to select → pick a random node (Added bc Masking created 'issues' with neighbor nodes)
            else:
                current = Utils.get_random_cell(maze, rows, cols)

            # Check if ALL neighbors have been visited; If so → Choose a random, unvisited node
            if Utils.is_node_in_list(visited, current.north_neighbor) and Utils.is_node_in_list(visited, current.east_neighbor) and Utils.is_node_in_list(
                    visited, current.south_neighbor) and Utils.is_node_in_list(visited, current.west_neighbor):

                # If there are nodes that have yet to be visited → Visit one at random
                if len(unvisited) >= 1:
                    current = unvisited[np.random.randint(0, len(unvisited))]

                # Otherwise → break
                else:
                    break

    return maze
