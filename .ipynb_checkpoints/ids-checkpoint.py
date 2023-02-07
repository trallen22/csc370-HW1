from puzzleboard import PuzzleBoard

def IDS(startBoard, maxDepth=0):
    GOALSTATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    nodes = 1
    for i in range(maxDepth):
        stack = []
        visited = {}
        stack.append(startBoard)
        while not (len(stack) == 0):
            curState = stack.pop()
            print("CURRENT STATE: ")
            print(curState)
            if curState == GOALSTATE:
                return curState.pathCost
            if curState.pathCost < i:
                for j in range(len(curState.getNextStates())):
                    nextState = curState.getNextStates()[j]
                    nodes += 1
                    #if (nextState.state not in visited) and (nextState not in stack):
                    stack.append(nextState)
    return False