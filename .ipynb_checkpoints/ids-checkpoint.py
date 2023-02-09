from puzzleboard import PuzzleBoard

def IDS(startBoard, maxDepth=0):
    GOALSTATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    nodes = 1
    for i in range(maxDepth):
        print("ITERATION: " + str(i))
        stack = []
        visited = []
        stack.append(startBoard)
        while not (len(stack) == 0):
            curState = stack.pop()
            visited.append(curState.state)
            print("CURRENT STATE: ")
            print(curState)
            if curState.state == GOALSTATE:
                return [nodes, curState.pathCost]
            if curState.pathCost < i:
                for j in range(len(curState.getNextStates())):
                    nextState = curState.getNextStates()[j]
                    nodes += 1
                    if not (nextState.state in visited or nextState in stack):
                        stack.append(nextState)
    return [-1, -1]