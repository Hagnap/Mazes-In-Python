import numpy as np

from Node import Node

'''
Maze Node values
    -1: Out of bounds or a masked node
    0: An open node
    1: A closed node (a wall)
'''

class Maze:
    def __init__(self, rows, cols, mask=None):

        self.maze = list()

        for i in range(rows):

            # Creates & adds a row (ie an empty list)
            self.maze.append(list())

            # Marks spot as open
            for j in range(cols):

                if mask[i][j] == 1:
                    self.maze[i].append(Node('-1', i, j))
                else:
                    self.maze[i].append(Node('0', i, j))

        # return

    def display_maze(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):

                # For masking
                if self.maze[i][j].value == '-1':
                    print(' ', end='\t')

                elif self.maze[i][j].value == '0':
                    print('O', end='\t')
                else:
                    # print(self.maze[i][j].value, end='\t')
                    print('■', end='\t')

            print()
        return
