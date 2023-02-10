from puzzleboard import PuzzleBoard
from queue import PriorityQueue
import random
from AStar import AStarH1
from tqdm import tqdm 


    
def batchPuzzles(size):
    puzzleDict = {}
    visited = {}
    checked = 0
    depths = list(range(2, 25, 2))
    pbar = tqdm(desc='puzzles solved', total = size)
    while checked < size:
        initialBoard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(initialBoard)
        curPuzzle = PuzzleBoard(initialBoard, 0)
        if (curPuzzle.solvable()):
            try:
                solved = visited[''.join(map(str, curPuzzle.state))]
            except KeyError:
                solved = AStarH1(curPuzzle, max(depths))
                visited[(''.join(map(str, curPuzzle.state)))] = solved
            solveDepth = solved[1]
            if (solveDepth % 2 == 0) and (solveDepth > 0):
                try:
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