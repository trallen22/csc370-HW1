from queue import PriorityQueue


# concept of A*
# parameters: 
#     startBoard - initial puzzleBoard object
#     heuristic - string for current heuristic -> 'h1', 'h2'
#     maxDepth - integer max depth to search for a solution; default 0 means no max depth
# returns: returns a list of total nodes created while running the algorithm
#           and the pathCost (representing depth) of the solution puzzleBoard 
def AStar(startBoard, heuristic, maxDepth=0):
    GOALSTATE = [0, 1, 2, 3, 4, 5, 6, 7, 8] # what we compare our current state to
    nodesCreated = 1
    order = 1
    stateQueue = PriorityQueue() # priority queue of board states
    stateQueue.put((0, 0, startBoard)) # priority queue compares by (path cost, order, curstate)
    visited = set() # using set to increase search time 
    while not (stateQueue.empty()):
        curState = stateQueue.get()[2]
        visited.add(''.join(map(str, curState.state))) # set can't hold list so have to convert to string
        if (maxDepth != 0) and (curState.pathCost > maxDepth):
            return [-1, -1]
        if curState.state == GOALSTATE:
            return [nodesCreated, curState.pathCost]
        # generates the next possible board states 
        for i in range(len(curState.getNextStates())):
            nextState = curState.getNextStates()[i] 
            if not (''.join(map(str, nextState.state)) in visited):
                # checks which heuristic to use
                if heuristic == 'h1':
                    stateQueue.put((nextState.pathCost + nextState.h1(), order, nextState))
                else:
                    stateQueue.put((nextState.pathCost + nextState.h2(), order, nextState))
                order += 1
            nodesCreated += 1 # keeps track of total nodes created
    return [nodesCreated, curState.pathCost]
