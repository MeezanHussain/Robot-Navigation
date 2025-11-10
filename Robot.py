from node import Node

STEP_COST = 1


class Robot:
    def __init__(self, grid):
        self.grid = grid

    def dfs_search(self, grid):
        frontier = [Node(grid.initial_state)]
        explored = list()
        no_of_nodes = 0

        while frontier:
            node = frontier.pop()
            if node.state not in explored:
                explored.append(node.state)
                no_of_nodes += 1

                if node.state in grid.goal_state:
                    return f"DFS\n<Node {node.state}> {no_of_nodes}\n{self.get_direction(node)}"

                for neighbor in grid.map.neighbors(node, explored)[::-1]:
                    if neighbor not in explored:
                        neighbor.path_cost = node.path_cost + STEP_COST
                        neighbor.depth = node.depth + 1
                        neighbor.action = self.get_action(node.state, neighbor.state)
                        neighbor.parent = node
                        node.children.append(neighbor)
                        frontier.append(neighbor)

        return f"DFS\nNo goal is reachable; {no_of_nodes}"

    def bfs_search(self, grid):
        frontier = [Node(grid.initial_state)]
        explored = list()
        no_of_nodes = 0

        while frontier:
            node = frontier.pop(0)
            if node.state not in explored:
                explored.append(node.state)
                no_of_nodes += 1

                if node.state in grid.goal_state:
                    return f"BFS\n<Node {node.state}> {no_of_nodes}\n{self.get_direction(node)}"

                for neighbor in grid.map.neighbors(node, explored):
                    if neighbor not in explored:
                        neighbor.path_cost = node.path_cost + STEP_COST
                        neighbor.depth = node.depth + 1
                        neighbor.action = self.get_action(node.state, neighbor.state)
                        neighbor.parent = node
                        node.children.append(neighbor)
                        frontier.append(neighbor)

        return f"BFS\nNo goal is reachable; {no_of_nodes}"

    def gbfs_heuristic(self, node):
        return min(
            abs(node.state[0] - goal[0]) + abs(node.state[1] - goal[1])
            for goal in self.grid.goal_state
        )

    def astar_heuristic(self, node):
        return (
            min(
                abs(node.state[0] - goal[0]) + abs(node.state[1] - goal[1])
                for goal in self.grid.goal_state
            )
            + node.path_cost
        )

    def new_astar_heuristic(self, node, goal):
        return (
            abs(node.state[0] - goal[0]) + abs(node.state[1] - goal[1]) + node.path_cost
        )

    def gbfs_search(self, grid):
        frontier = [Node(grid.initial_state)]
        explored = list()
        no_of_nodes = 0

        while frontier:
            node = frontier.pop(0)
            if node.state not in explored:
                explored.append(node.state)
                no_of_nodes += 1

                if node.state in grid.goal_state:
                    return f"GBFS\n<Node {node.state}> {no_of_nodes}\n{self.get_direction(node)}"

                for neighbor in grid.map.neighbors(node, explored):
                    if neighbor not in explored:
                        neighbor.path_cost = node.path_cost + STEP_COST
                        neighbor.depth = node.depth + 1
                        neighbor.action = self.get_action(node.state, neighbor.state)
                        neighbor.parent = node
                        node.children.append(neighbor)
                        frontier.append(neighbor)
                frontier.sort(key=self.gbfs_heuristic)

        return f"GBFS\nNo goal is reachable; {no_of_nodes}"

    def a_star(self, grid):
        frontier = [Node(grid.initial_state)]
        explored = list()
        no_of_nodes = 0

        while frontier:
            node = frontier.pop(0)
            if node.state not in explored:
                explored.append(node.state)
                no_of_nodes += 1

                if node.state in grid.goal_state:
                    return f"ASTAR\n<Node {node.state}> {no_of_nodes}\n{self.get_direction(node)}"

                for neighbor in grid.map.neighbors(node, explored):
                    if neighbor not in explored:
                        neighbor.path_cost = node.path_cost + STEP_COST
                        neighbor.depth = node.depth + 1
                        neighbor.action = self.get_action(node.state, neighbor.state)
                        neighbor.parent = node
                        node.children.append(neighbor)
                        frontier.append(neighbor)
                frontier.sort(key=self.astar_heuristic)

        return f"ASTAR\nNo goal is reachable; {no_of_nodes}"

    def new_a_star(self, grid, goal):
        frontier = [Node(grid.initial_state)]
        explored = list()

        while frontier:
            node = frontier.pop(0)
            if node.state not in explored:
                explored.append(node.state)
                if node.state == goal:
                    return node.state, self.get_direction(node)

                for neighbor in grid.map.neighbors(node, explored):
                    if neighbor not in explored:
                        neighbor.path_cost = node.path_cost + STEP_COST
                        neighbor.depth = node.depth + 1
                        neighbor.action = self.get_action(node.state, neighbor.state)
                        neighbor.parent = node
                        node.children.append(neighbor)
                        frontier.append(neighbor)
                frontier.sort(key=lambda x: self.new_astar_heuristic(x, goal))
        return False, None

    def research_algorithm(self, grid):
        all_goals_found = False
        total_path = []
        goal_nodes = []
        for state in grid.goal_state:
            goal_nodes.append(Node(state))
        initial_node = Node(grid.initial_state)
        goal_nodes.sort(key=lambda x: self.new_astar_heuristic(initial_node, x.state))
        grid.goal_state = [node.state for node in goal_nodes]
        while not all_goals_found:
            if len(grid.goal_state) == 0:
                all_goals_found = True
                continue
            goal = grid.goal_state.pop(0)
            new_path = self.new_a_star(grid, goal)
            if new_path[0]:
                grid.initial_state = new_path[0]
                total_path.append(new_path)
        if len(total_path) == 0:
            return False, None
        return total_path

    def get_action(self, current_pos, next_pos):
        if next_pos[0] == current_pos[0] + 1:
            return "right"
        elif next_pos[0] == current_pos[0] - 1:
            return "left"
        elif next_pos[1] == current_pos[1] + 1:
            return "down"
        elif next_pos[1] == current_pos[1] - 1:
            return "up"

    def get_direction(self, node):
        node_parent = node
        directions = []
        while node_parent.parent is not None:
            directions.append(node_parent.action)
            node_parent = node_parent.parent
        return directions[::-1]
