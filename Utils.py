import random
import os

from Node import Node

def get_maze_type():

    # Prompt user for type of maze
    print('Maze Types')
    print('\t1) Binary Tree Maze')
    print('\t2) Sidewinder Maze')
    print('\t3) Aldous-Broder Maze')
    print('\t4) Wilson\'s Maze')
    print('\t5) Hunt and Kill Maze')
    print('\t6) Recursive Backtracker Maze')
    maze_type = int(input('Select Maze Type: '))

    return maze_type

def is_node_in_list(node_list, node):

    for i, v in enumerate(node_list):
        # Check if current node is our node of interest
        if node.row == node_list[i].row and node.col == node_list[i].col:
            return True

    return False

def update_neighbors(maze, rows, cols):

    for i in range(rows):
        for j in range(cols):

            # Boundary Checks

            # North
            if i > 0 and maze[i - 1][j].value == '0':
                maze[i][j].north_neighbor = maze[i - 1][j]
            else:
                maze[i][j].north_neighbor = Node('-1', -1, -1)

            # East
            if j < cols - 1 and maze[i - 1][j].value == '0':
                maze[i][j].east_neighbor = maze[i][j + 1]
            else:
                maze[i][j].east_neighbor = Node('-1', -1, -1)

            # South
            if i < rows - 1 and maze[i - 1][j].value == '0':
                maze[i][j].south_neighbor = maze[i + 1][j]
            else:
                maze[i][j].south_neighbor = Node('-1', -1, -1)

            # West
            if j > 0 and maze[i - 1][j].value == '0':
                maze[i][j].west_neighbor = maze[i][j - 1]
            else:
                maze[i][j].west_neighbor = Node('-1', -1, -1)

    return maze

def get_neighbors(node):

    neighbors = list()

    if node.north_neighbor.value != '-1':
        neighbors.append(node.north_neighbor)
    else:
        pass

    if node.east_neighbor.value != '-1':
        neighbors.append(node.east_neighbor)
    else:
        pass

    if node.south_neighbor.value != '-1':
        neighbors.append(node.south_neighbor)
    else:
        pass

    if node.west_neighbor.value != '-1':
        neighbors.append(node.west_neighbor)
    else:
        pass

    return neighbors

def get_random_cell(maze, rows, cols):

    # Get random coordinate
    x = random.randint(0, rows - 1)
    y = random.randint(0, cols - 1)

    # Return random coordinate
    return maze[x][y]

def load_mask_from_file(mask):

    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'Mask.txt')
    file = open(filename, 'r')
    lines = file.readlines()

    index = 0

    for line in lines:

        nested_index = 0

        for character in line:

            if character != '\n':

                if character != '0':

                    mask[index][nested_index] = 1

            nested_index += 1

        index += 1

    file.close()

    return mask
