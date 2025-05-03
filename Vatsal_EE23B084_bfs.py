## TEAM ANVESHAK 2024-25, CFI, IIT MADRAS ##
## POINT ROBOT MOTION PLANNING TASK 1 ##

## BREADTH FIRST SEARCH ##


## USE THESE LIBRARIES, YOU WON'T NEED ANY OTHER AND YOU ARE NOT SUPPOSED TO USE TOO ##
import math
import numpy as np
from maze import Maze
import traceback 

parent = {}
paths_poss = {}

def breadthFirstSearch(start, goal, m):
    closed_list = []
    visited_set = set()
    open_list = [start]

    m.visualize_map()

    while open_list:
        m.update_visualization(open_list, closed_list)
        node = open_list.pop(0)
        closed_list.append(node)
        visited_set.add(node)
        successor = m.get_successors(node)
        for i in successor:
            if i not in visited_set:
                open_list.append(i)
                visited_set.add(i)
                paths_poss[i] = node	
                
            if goal in closed_list: 
                break
              	
    paths_poss[start] = (start[0] - 1, start[1] - 1)
    cell = goal
    if goal not in paths_poss:
        print("..........Failure to find a path..........")
        raise KeyError("Failure")
        

    while cell != start:
        parent[paths_poss[cell]] = cell
        cell = paths_poss[cell]
    if cell == start:
        parent[paths_poss[cell]] = cell
    return list(parent.values())	

if __name__ == "__main__":
    m = Maze(map_num=1)   ## TOGGLE BETWEEN 1 AND 2 TO TEST IN BOTH ENVIRONMENTS 

    m.load_map()

    #m.visualize_map() ### UNCOMMENT THIS TO JUST VIEW THE MAZE, AND plt.show() IN MAZE.PY LINE 52, ALSO COMMENT THE BELOW 3 LINES TOO

    ### COMMENT THESE TO JUST VIEW THE MAZE
    path = breadthFirstSearch(m.get_start_state(), m.get_goal_state(), m)
    print("Number of Steps taken by the Robot:", len(path))
    m.keep_plot_open(path)

