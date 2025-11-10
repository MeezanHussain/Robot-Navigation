from node import Node

class Map:
    def __init__(self):
        self.length, self.width = 0, 0
        self.wall_list = []

    def is_useable(self, node):
        x = node.state[0]
        y = node.state[1]
        is_wall = self.is_wall(node)
        return not is_wall and self.is_within_boundary(node)

    def is_within_boundary(self, node):
        x = node.state[0]
        y = node.state[1]
        if 0 <= x < self.width and 0 <= y < self.length:
            return True
        return False

    def is_wall(self, node):
        x = node.state[0]
        y = node.state[1]
        string_coordinate = (x,y)
        if string_coordinate in self.wall_list:
            return True
        return False

    def neighbors(self, node, explored):
        useable_neighbors = []
        x = node.state[0]
        y = node.state[1]
        neighbors = [(x, y-1), (x-1, y), (x, y+1), (x+1, y)]
        for neighbor in neighbors:
            if neighbor not in explored:
                neighbor_node = Node(neighbor)
                if self.is_useable(neighbor_node):
                    useable_neighbors.append(neighbor_node)
        return useable_neighbors

