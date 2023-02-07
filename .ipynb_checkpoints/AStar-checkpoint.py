from queue import PriorityQueue


# concept of A* using h1
def AStarH1(startBoard, maxDepth=0):
    GOALSTATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    nodesCreated = 1
    order = 1
    stateQueue = PriorityQueue()
    stateQueue.put((0, 0, startBoard))
    visited = []
    while not (stateQueue.empty()):
        curState = stateQueue.get()[2]
        visited.append(curState.state)
        print("TESTING STATE: ")
        print(curState)
        if (maxDepth != 0) and (curState.pathCost > maxDepth):
            return [-1, -1]
        if curState.state == GOALSTATE:
            return [nodesCreated, curState.pathCost]
        for i in range(len(curState.getNextStates())):
            nextState = curState.getNextStates()[i]
            if not (nextState.state in visited):
                stateQueue.put((nextState.pathCost + nextState.h1(), order, nextState))
                order += 1
            nodesCreated += 1
    return [nodesCreated, curState.pathCost]


# concept of A* using h2
def AStarH2(startBoard):
    GOALSTATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    nodesCreated = 1
    order = 1
    stateQueue = PriorityQueue()
    stateQueue.put((0, 0, startBoard))
    while not (stateQueue.empty()):
        curState = stateQueue.get()[2]
        if curState.state == GOALSTATE:
            return nodesCreated
        for i in range(len(curState.getNextStates())):
            nextState = curState.getNextStates()[i]
            stateQueue.put((nextState.pathCost + nextState.h2(), order, nextState))
            order += 1
            nodesCreated += 1
        if nodesCreated > 20:
            return nodesCreated
    return nodesCreated

