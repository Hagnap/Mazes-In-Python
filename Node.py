class Node:

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

        self.parent = None
        self.north_neighbor = None
        self.east_neighbor = None
        self.south_neighbor = None
        self.west_neighbor = None
