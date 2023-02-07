from queue import PriorityQueue
from puzzleboard import PuzzleBoard
from AStar import AStarH1, AStarH2
from generateRandomPuzzle import batchPuzzles
from tabulate import tabulate 
from ids import IDS

# goal state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

initialState = [1, 2, 0,
                3, 4, 5, 
                6, 7, 8]

b = PuzzleBoard(initialState, 0)

print("INITIAL STATES: ")
print(b)
print(b.solvable())

print(IDS(b, 5))

# print(generatePuzzle(3))

# print(AStarH1(b))

# print(AStarH2(b))
# x = batchPuzzles(1200) 
# data = []
# for i in range(2, 25, 2):
#     try:
#         data.append([i, sum(x[i]) / len(x[i]), len(x[i])])
#     except:
#         data.append([i, 'na', 0])
# colHeaders = ['d', 'A*(h1)', 'total']
# print(tabulate(data, headers=colHeaders, tablefmt='simple'))

# # for i in range(len(x)):
#     print(x.state)