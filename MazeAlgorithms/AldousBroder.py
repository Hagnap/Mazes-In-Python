import random
import numpy as np

import Utils

def AldousBroderMazeAlgorithm(maze, mask, rows, cols):
    visited = list()

    # Choose a random node to start at
    current = Utils.get_random_cell(maze, rows, cols)

    while len(visited) + np.count_nonzero(mask) <= ((rows * cols) - 1):

        if not Utils.is_node_in_list(visited, current):

            print(f'Visiting new node! {len(visited) + 1} / {(rows * cols)}')

            # Randomly set the node to a wall
            rand_wall = random.random()
            if rand_wall >= 0.625:
                # current.value = '■'
                if mask[current.row][current.col] == 0:
                    maze[current.row][current.col].value = '■'

            # Add current to visited
            visited.append(current)

        # Gets Neighbors
        neighbors = Utils.get_neighbors(current)

        # Select a neighbor at random
        if len(neighbors) > 0:
            rand_neighbor = np.random.randint(0, len(neighbors))
            print(f'{rand_neighbor} -- Out of Indices: {len(neighbors) - 1} ({len(neighbors)})')
            current = neighbors[rand_neighbor]

        # If there is no neighbor to select → pick a random node (Added bc Masking created 'issues' with neighbor nodes)
        else:
            current = Utils.get_random_cell(maze, rows, cols)

    return maze
