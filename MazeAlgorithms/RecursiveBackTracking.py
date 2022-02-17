import numpy as np
import random

import Utils

def RecursiveBackTrackingMazeAlgorithm(maze, mask, rows, cols):

    stack = list()

    # Idea: Look for visited nodes, when one is found start at a random unvisited node
    visited = list()
    unvisited = list()

    # Stores the nodes for backtracking
    backtrack = None

    # Choose a random node to start at
    current = Utils.get_random_cell(maze, rows, cols)

    # Before creating the maze, add each node to the unvisited list
    for i in range(rows):
        for j in range(cols):
            unvisited.append(maze[i][j])
    # print(len(unvisited))

    while len(unvisited) - np.count_nonzero(mask) > 0:

        #print(f'Unvisited Nodes: {len(unvisited) - np.count_nonzero(mask)}')

        # If we are using a mask and this node has been 'killed' → ignore it
        #if mask[current.row][current.col] != 0:
            #continue

        # If the node has yet to be visited, mark it as visited and add it to the stack
        if Utils.is_node_in_list(unvisited, current):
            unvisited.remove(current)
            visited.append(current)
            stack.append(current)

            # Randomly add a wall
            rand_wall = random.random()
            if rand_wall >= 0.625:
                if mask[current.row][current.col] == 0:
                    maze[current.row][current.col].value = '■'

        # Otherwise → Get the neighbors of the current cell
        else:

            # Get neighbors
            neighbors = Utils.get_neighbors(current)

            # Select a neighbor at random (Faces similar issue as the AldousBroderMazeAlgorithm)
            if len(neighbors) > 0:
                rand_neighbor = np.random.randint(0, len(neighbors))
                #print(f'{rand_neighbor} -- Out of Indices: {len(neighbors) - 1} ({len(neighbors)})')
                current = neighbors[rand_neighbor]

            # If there is no neighbor to select → pick a random node (Added bc Masking created 'issues' with neighbor nodes)
            else:

                # Done to help with infinite loops (Encourages visits unvisited nodes when there are few left)
                # If there are 10 or more unvisited nodes → choose a random node.
                if len(unvisited) >= 10:
                    current = Utils.get_random_cell(maze, rows, cols)

                # Otherwise, choose a random,unvisited Node
                else:
                    current = unvisited[random.randint(0, len(unvisited) - 1)]


        # Check if ALL neighbors have been visited; If so → Choose a random, unvisited node
        if Utils.is_node_in_list(visited, current.north_neighbor) and Utils.is_node_in_list(visited, current.east_neighbor) and Utils.is_node_in_list(visited, current.south_neighbor) and Utils.is_node_in_list(visited, current.west_neighbor):

            # BACKTRACK
            while True:

                print('*')

                # Backtrack until a node with an unvisited neighbor is found
                if len(stack) > 1:
                    backtrack = stack[-1]
                    stack.remove(stack[-1])

                    neighbors = Utils.get_neighbors(backtrack)
                else:
                    break

                # Check to see if any neighbors have been visited (if so, remove them)
                for node in neighbors:
                    if Utils.is_node_in_list(visited, node):
                        neighbors.remove(node)

                # If there is a neighbor that we can select, choose one at random & End loop
                if len(neighbors) > 0:
                    current = neighbors[np.random.randint(0, len(neighbors))]
                    break

                # No neighbor to select, choose a random-unvisited node, and end loop
                else:
                    print('OOF')

                    # Done to help with infinite loops (Encourages visits unvisited nodes when there are few left -- Same as seen above)
                    if len(unvisited) >= 10:
                        current = Utils.get_random_cell(maze, rows, cols)
                    else:
                        current = unvisited[random.randint(0, len(unvisited) - 1)]

                    break

    return maze
