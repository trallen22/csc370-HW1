from puzzleboard import PuzzleBoard
from queue import PriorityQueue
import random
from AStar import AStar
from tqdm import tqdm 
from ids import IDS


# Generates a certain number of puzzleBoards and creates a dictionary with specified depths 
# as the keys and a list of the number of nodes created for each solved board at that depth. 
# parameters: 
#     size - integer the total number of puzzleBoards with the specified depths 
#     heuristic - string for which heuristic to use when solving each puzzleBoard 
# returns: returns a dictionary with solve depths as the keys and the number of nodes 
#           created for the puzzleBoards with that solve depth
def batchPuzzles(size, heuristic):
    puzzleDict = {} # dictionary to hold -> {solve depth: a list of nodes created for all solved boards with same solve depth}
    visited = {} # dictionary to hold -> {string of the current state:[nodes created, solve depth]}
    checked = 0 # number of board cells that are added to puzzleDict
    if heuristic == 'ids':
        depths = list(range(2, 13, 2))
    else:
        depths = list(range(2, 25, 2))
    # this is a progress bar to check while running in terminal
    pbar = tqdm(desc='puzzles solved for ' + heuristic, total = size)
    while checked < size:
        # creates a board and shuffles it
        initialBoard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(initialBoard)
        curPuzzle = PuzzleBoard(initialBoard, 0)
        if (curPuzzle.solvable()): # check to make sure puzzle is solvable
            # used try and except to index the dictionary value to 
            # increase the speed of checking for values
            try:
                solved = visited[''.join(map(str, curPuzzle.state))] # dictionaries can't hold sets as keys
            except KeyError:
                if heuristic == 'h1':
                    solved = AStar(curPuzzle, heuristic, max(depths))
                elif heuristic == 'h2':
                    solved = AStar(curPuzzle, heuristic, max(depths))
                else:
                    solved = IDS(curPuzzle, max(depths))
                visited[(''.join(map(str, curPuzzle.state)))] = solved
            solveDepth = solved[1] # solved[1] is pathCost of board cell
            if (solveDepth % 2 == 0) and (solveDepth > 0):
                try: # same try except logic as line 28
                    if (len(puzzleDict[solveDepth]) < 100): # stopes 
                        puzzleDict[solveDepth].append(solved[0])
                        # takes the current solve depth out of list of 
                        # depths once 100 puzzles are found
                        if len(puzzleDict[solveDepth]) == 100: 
                            depths.remove(solveDepth)
                        pbar.update(1)
                        checked += 1
                except KeyError:
                    puzzleDict[solveDepth] = [solved[0]]
                    pbar.update(1)
                    checked += 1
    return puzzleDict