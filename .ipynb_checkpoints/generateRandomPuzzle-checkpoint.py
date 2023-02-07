from puzzleboard import PuzzleBoard
from queue import PriorityQueue
import random
from AStar import AStarH1
from tqdm import tqdm 


    
def batchPuzzles(size):
    puzzleDict = {}
    # visited = []
    checked = 0
    depths = list(range(2, 25, 2))
    pbar = tqdm(desc='While loop', total = size)
    while checked < size:
        initialBoard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(initialBoard)
        curPuzzle = PuzzleBoard(initialBoard, 0)
        # if not (initialBoard in visited):
        #     visited.append(initialBoard)
        if (curPuzzle.solvable()):
            solved = AStarH1(curPuzzle, max(depths))
            solveDepth = solved[1]
            if (solveDepth % 2 == 0):
                if solveDepth in puzzleDict:
                    if (len(puzzleDict[solveDepth]) <= 99):
                        puzzleDict[solveDepth].append(solved[0])
                        checked += 1
                        pbar.update(1)
                        if len(puzzleDict[solveDepth]) == 100:
                            depths.remove(solveDepth)
                else:
                    puzzleDict[solveDepth] = [solved[0]]
                    checked += 1
                    pbar.update(1)
                print("DICTIONARY: ")
                print(puzzleDict)
    return puzzleDict