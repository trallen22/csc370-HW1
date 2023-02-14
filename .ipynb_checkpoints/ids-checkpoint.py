from puzzleboard import PuzzleBoard

# concept of ids 
# parameters: 
#     startBoard - initial puzzleBoard object
#     maxDepth - integer max depth to search for a solution; default 0 means no max depth
# returns: returns a list of total nodes created while running the algorithm
#           and the pathCost (representing depth) of the solution puzzleBoard 
def IDS(startBoard, maxDepth=0):
    GOALSTATE = [0, 1, 2, 3, 4, 5, 6, 7, 8] # goal to compare to
    nodes = 1
    for i in range(maxDepth):
        stack = []
        visited = set() # using a set to increase search speed
        stack.append(startBoard)
        visited.add(''.join(map(str, startBoard.state))) # sets can only hold strings, not lists
        while not (len(stack) == 0):
            curState = stack.pop()
            if curState.state == GOALSTATE:
                return [nodes, curState.pathCost]
            if curState.pathCost <= i: # stop searching at current iteration max depth
                for j in range(len(curState.getNextStates())):
                    nextState = curState.getNextStates()[j]
                    nodes += 1
                    if not (''.join(map(str, nextState.state)) in visited):
                        stack.append(nextState)
                        visited.add(''.join(map(str, nextState.state)))
    return [-1, -1]