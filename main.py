from resource_Initialize import ResourceInitialize
from map import Map
from Robot import Robot

def main(filename, algorithm, len_sys):
    map_instance = Map()
    grid = ResourceInitialize(filename, map_instance)
    grid.populate_data()
    ai = Robot(grid)

    if len_sys > 1:
        method = algorithm.lower()
        if method == "dfs":
            print(ai.dfs_search(grid))
        elif method == "bfs":
            print(ai.bfs_search(grid))
        elif method == "gbfs":
            print(ai.gbfs_search(grid))
        elif method == "astar":
            print(ai.a_star(grid))
        elif method == "research":
            path = ai.research_algorithm(grid)
            print("RESEARCH ALGORITHM")
            if path[0]:
                print(path)
            else:
                print("No Goal Reachable")
        else:
            print("No goal is reachable")
    else:
        print("No arguments provided.")
