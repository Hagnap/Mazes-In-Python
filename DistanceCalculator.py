import sys
import random

class DistanceCalculator:

    def __init__(self, maze):

        self.distances = list()

        for i in range(len(maze)):

            distance_list = list()
            for j in range(len(maze[i])):

                if maze[i][j].value == '0':
                    distance_list.append(-1)
                else:
                    distance_list.append(sys.maxsize)

            self.distances.append(distance_list)

    def generate_distances(self, maze, start_pos, rows, cols):

        frontier = list()
        visited = list()

        #x = random.randint(0, rows-1)
        #y = random.randint(0, cols-1)

        #x = int(rows / 2)
        #y = int(cols / 2)

        x = start_pos[0]
        y = start_pos[1]

        current = maze[x][y]
        # current = maze[0][0]

        # Check if we start at an open node or not
        if current.value == '0':
            self.distances[current.row][current.col] = 0
        else:
            self.distances[current.row][current.col] = sys.maxsize

        # Add current to the frontier list
        frontier.append(current)

        # Start loop
        while len(frontier) > 0:

            # Gets the current node from the frontier
            current = frontier[0]

            # North
            if (current.north_neighbor.value == '0') and (current.north_neighbor not in visited):
                frontier.append(current.north_neighbor)
                current.north_neighbor.parent = current

                if current.parent is None:
                    self.distances[current.row - 1][current.col] = 1
                else:
                    self.distances[current.row - 1][current.col] = self.distances[current.row][current.col] + 1

            # East
            if (current.east_neighbor.value == '0') and (current.east_neighbor not in visited):
                frontier.append(current.east_neighbor)
                current.east_neighbor.parent = current

                if current.parent is None:
                    self.distances[current.row][current.col + 1] = 1
                else:
                    self.distances[current.row][current.col + 1] = self.distances[current.row][current.col] + 1

            # South
            if (current.south_neighbor.value == '0') and (current.south_neighbor not in visited):
                frontier.append(current.south_neighbor)
                current.south_neighbor.parent = current

                if current.parent is None:
                    self.distances[current.row + 1][current.col] = 1
                else:
                    self.distances[current.row + 1][current.col] = self.distances[current.row][current.col] + 1

            # West
            if (current.west_neighbor.value == '0') and (current.west_neighbor not in visited):
                frontier.append(current.west_neighbor)
                current.west_neighbor.parent = current

                if current.parent is None:
                    self.distances[current.row][current.col - 1] = 1
                else:
                    self.distances[current.row][current.col - 1] = self.distances[current.row][current.col] + 1

            # Update Visited & Frontier
            frontier.remove(current)
            visited.append(current)

        return

    def display_costs(self):
        for i in range(len(self.distances)):
            for j in range(len(self.distances[i])):
                if self.distances[i][j] == sys.maxsize:
                    print('X', end='\t')
                else:
                    print(self.distances[i][j], end='\t')
            print()