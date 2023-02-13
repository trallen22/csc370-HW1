from puzzleboard import PuzzleBoard

def IDS(startBoard, maxDepth=0):
    GOALSTATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    nodes = 1
    for i in range(maxDepth):
        stack = []
        visited = set() # set to increase search speed
        stack.append(startBoard)
        visited.add(''.join(map(str, startBoard.state)))
        while not (len(stack) == 0):
            curState = stack.pop()
            if curState.state == GOALSTATE:
                return [nodes, curState.pathCost]
            if curState.pathCost <= i:
                for j in range(len(curState.getNextStates())):
                    nextState = curState.getNextStates()[j]
                    nodes += 1
                    if not (''.join(map(str, nextState.state)) in visited):
                        stack.append(nextState)
                        visited.add(''.join(map(str, nextState.state)))
    return [-1, -1]