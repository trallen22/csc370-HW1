from puzzleboard import PuzzleBoard
from queue import PriorityQueue
import random
from AStar import AStar
from tqdm import tqdm 
from ids import IDS


    
def batchPuzzles(size, heuristic):
    puzzleDict = {} # dictionary to hold -> {solve depth:list(nodes created)
    visited = {} # dictionary to hold -> {str(current state):[nodes created, solve depth]}
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
                    if (len(puzzleDict[solveDepth]) < 100):
                        puzzleDict[solveDepth].append(solved[0])
                        if len(puzzleDict[solveDepth]) == 100:
                            depths.remove(solveDepth)
                        pbar.update(1)
                        checked += 1
                except KeyError:
                    puzzleDict[solveDepth] = [solved[0]]
                    pbar.update(1)
                    checked += 1
    return puzzleDict