class Node:
    def __init__(self, state, parent=None, children=list(), action=None, path_cost=0, depth=0):
        self.state = state
        self.parent = parent
        self.children = children
        self.action = action
        self.path_cost = path_cost
        self.depth = depth

