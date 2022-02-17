import numpy as np
import sys
import random

import Utils
from DistanceCalculator import DistanceCalculator
from Maze import Maze

from MazeAlgorithms import Test
from MazeAlgorithms import BinaryTree
from MazeAlgorithms import Sidewinder
from MazeAlgorithms import AldousBroder
from MazeAlgorithms import Wilsons
from MazeAlgorithms import HuntAndKill
from MazeAlgorithms import RecursiveBackTracking


if __name__ == '__main__':

    print('Starting execution...')

    # Prompt user for maze dimensions
    print('Please enter the desired dimensions')
    rows = int(input('\tNumber of Rows: '))
    cols = int(input('\tNumber of Columns: '))
    print()

    maze_type = Utils.get_maze_type()

    # Prompt user to see if they want a mask
    mask_input = 3 # set mask_input to 3 initially so it loops
    mask = np.zeros((rows, cols), dtype=np.int64)  # 0 by default but alters values if needed

    while mask_input == 3:
        print('Mask Options')
        print('\t1) Yes\n\t2) No\n\t3) What is a mask?')
        mask_input = int(input('Select Mask Option: '))

        if mask_input == 1:
            print('A mask will be used.')

            # Kills the cells used in the mask
            #mask[0][0] = 1
            #mask[1][1] = 1
            #mask[0][-1] = 1
            #mask[1][-2] = 1

            mask = Utils.load_mask_from_file(mask)

        elif mask_input == 2:
            print('No mask will be used.')

        elif mask_input == 3:
            print(f'A mask is a... Finish later')

        else:
            print('Invalid Input, no mask will be used.')

    print('\nMask:')
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            print(mask[i][j], end='\t')
        print()

    print('\nEmpty Maze with Mask:')
    maze = Maze(rows, cols, mask)
    maze.display_maze()

    # Update neighbors for each cell (Want to add references to nodes and kill cells used in the mask)
    Utils.update_neighbors(maze.maze, rows, cols)
    ### neighbors = Utils.get_neighbors(maze.maze[1][1])

    # Adds wall using specified maze algorithm
    if maze_type == 1:
        maze.maze = BinaryTree.BinaryTreeMazeAlgorithm(maze.maze)
    elif maze_type == 2:
        maze.maze = Sidewinder.SidewinderMazeAlgorithm(maze.maze)
    elif maze_type == 3:
        maze.maze = AldousBroder.AldousBroderMazeAlgorithm(maze.maze, mask, rows, cols)
    elif maze_type == 4:
        maze.maze = Wilsons.WilsonsMazeAlgorithm(maze.maze, mask, rows, cols)
    elif maze_type == 5:
        maze.maze = HuntAndKill.HuntAndKillMazeAlgorithm(maze.maze, mask, rows, cols)
    elif maze_type == 6:
        maze.maze = RecursiveBackTracking.RecursiveBackTrackingMazeAlgorithm(maze.maze, mask, rows, cols)
    else:
        maze.maze = Test.TestMazeAlgorithm(maze.maze)

    # Random Starting Point
    x = random.randint(0, rows-1)
    y = random.randint(0, cols-1)
    start_pos = [x, y]

    # Instantiate a DistanceCalculator object to generate & display distance array
    print('Generating distances....')
    dijkstras = DistanceCalculator(maze.maze)
    print(f'Dimensions: ({rows}:{len(maze.maze)} -- {cols}:{len(maze.maze[0])})')
    dijkstras.generate_distances(maze.maze, start_pos, rows, cols)
    dijkstras.display_costs()

    print('\nMaze:')
    maze.display_maze()

    print('\nTerminating program...')
