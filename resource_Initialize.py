from map import Map


class ResourceInitialize:
    def __init__(self, testfile, map):
        self.file = open(testfile, "r")
        self.wall = []
        self.dimensions = ()
        self.initial_state = ()
        self.goal_state = []
        self.map = map

    def generate_wall(self, one_wall):
        x, y, w, h = one_wall[0], one_wall[1], one_wall[2], one_wall[3]
        for j in range(y, y + h):
            for i in range(x, x + w):
                self.wall.append((i, j))

    def populate_data(self):
        lines = self.file.readlines()
        self.dimensions = lines[0].strip()
        self.initial_state = eval(lines[1].strip())
        self.goal_state = lines[2].strip().split("|")
        for i in range(len(self.goal_state)):
            self.goal_state[i] = eval(self.goal_state[i])
        walls = [eval(i) for i in lines[3:]]
        for wall in walls:
            self.generate_wall(wall)
        self.map.wall_list = self.wall
        self.dimensions = eval(self.dimensions)
        self.map.length = self.dimensions[0]
        self.map.width = self.dimensions[1]

    def close_file(self):
        self.file.close()
