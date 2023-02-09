from queue import PriorityQueue
from puzzleboard import PuzzleBoard
from AStar import AStarH1, AStarH2
from generateRandomPuzzle import batchPuzzles
from tabulate import tabulate 
from ids import IDS

# goal state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

initialState = [1, 4, 2,
                3, 5, 8, 
                6, 7, 0]

b = PuzzleBoard(initialState, 0)

print("INITIAL STATES: ")
print(b)
print(b.solvable())

data = [[0, 23, 4], [4,2,1]]
colHeaders = ['a', 'b', 'c']



#print(IDS(b, 5))

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
# with open("newFile.txt", 'a') as f:
#     f.write('another \n')
#     f.write(str(tabulate(data, headers=colHeaders, tablefmt='simple')))
# print(tabulate(data, headers=colHeaders, tablefmt='simple'))

from sympy import symbols, solve
xx = symbols('x')
nodes = 52
depth = 5
f = 0
f -= nodes + 1
for i in range(depth + 1):
    f += xx**i
print(f)
bfactor = solve(f)
print(bfactor)