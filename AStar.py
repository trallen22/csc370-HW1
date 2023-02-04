from queue import PriorityQueue


# concept of A* using h1
def AStarH1(startBoard):
    GOALSTATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    nodesCreated = 1
    order = 1
    stateQueue = PriorityQueue()
    stateQueue.put((0, 0, startBoard))
    while not (stateQueue.empty()):
        curState = stateQueue.get()[2]
        print("TESTING STATE h1: ")
        print(curState)
        if curState.state == GOALSTATE:
            return nodesCreated
        for i in range(len(curState.getNextStates())):
            nextState = curState.getNextStates()[i]
            stateQueue.put((nextState.pathCost + nextState.h2(), order, curState.getNextStates()[i]))
            order += 1
            nodesCreated += 1
        if nodesCreated > 20:
            return nodesCreated
    return nodesCreated


# concept of A* using h2
def AStarH2(startBoard):
    GOALSTATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    nodesCreated = 1
    order = 1
    stateQueue = PriorityQueue()
    stateQueue.put((0, 0, startBoard))
    while not (stateQueue.empty()):
        curState = stateQueue.get()[2]
        print("TESTING STATE h2: ")
        print(curState)
        if curState.state == GOALSTATE:
            return nodesCreated
        for i in range(len(curState.getNextStates())):
            nextState = curState.getNextStates()[i]
            stateQueue.put((nextState.pathCost + nextState.h2(), order, curState.getNextStates()[i]))
            order += 1
            nodesCreated += 1
        if nodesCreated > 20:
            return nodesCreated
    return nodesCreated

