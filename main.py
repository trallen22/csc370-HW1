from queue import PriorityQueue
from puzzleboard import PuzzleBoard
from AStar import AStar
from generateRandomPuzzle import batchPuzzles
from tabulate import tabulate 
from ids import IDS

# goal state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

initialState = [1, 4, 2,
                3, 5, 8, 
                6, 7, 0]

# b = PuzzleBoard(initialState, 0)

# print("INITIAL STATES: ")
# print(b)
# print(b.solvable())

ids = batchPuzzles(600, 'ids')
idsdata = []
for i in range(2, 13, 2):
    try:
        idsdata.append([i, sum(ids[i]) / len(ids[i]), len(ids[i])])
    except:
        idsdata.append([i, 'na', 0])
idscolHeaders = ['d', 'IDS', 'total ids']
with open("newFile.txt", 'a') as f:
    f.write(str(tabulate(idsdata, headers=idscolHeaders, tablefmt='simple')))
print(tabulate(idsdata, headers=idscolHeaders, tablefmt='simple'))
        
# h1 = batchPuzzles(1200, 'h1') 
# h2 = batchPuzzles(1200, 'h2')
# ids = batchPuzzles(600, 'ids')

# h1data = []
# h2data = []
# idsdata = []
# for i in range(2, 25, 2):
#     try:
#         h1data.append([i, sum(h1[i]) / len(h1[i]), len(h1[i])])
#     except:
#         h1data.append([i, 'na', 0])
#     try:
#         h2data.append([i, sum(h2[i]) / len(h2[i]), len(h2[i])])
#     except:
#         h2data.append([i, 'na', 0])
# for i in range(2, 13, 2):
#     try:
#         idsdata.append([i, sum(ids[i]) / len(ids[i]), len(ids[i])])
#     except:
#         idsdata.append([i, 'na', 0])
# h1colHeaders = ['d', 'A*(h1)', 'total h1']
# h2colHeaders = ['d', 'A*(h2)', 'total h2']
# idscolHeaders = ['d', 'IDS', 'total ids']
# with open("newFile.txt", 'a') as f:
#     f.write(str(tabulate(h1data, headers=h1colHeaders, tablefmt='simple')))
#     f.write(str(tabulate(h2data, headers=h2colHeaders, tablefmt='simple')))
#     f.write(str(tabulate(idsdata, headers=idscolHeaders, tablefmt='simple')))
# print(tabulate(h1data, headers=h1colHeaders, tablefmt='simple'))
# print()
# print(tabulate(h2data, headers=h2colHeaders, tablefmt='simple'))
# print()
# print(tabulate(idsdata, headers=idscolHeaders, tablefmt='simple'))

# from sympy import symbols, solve
# xx = symbols('x')
# nodes = 52
# depth = 5
# f = 0
# f -= nodes + 1
# for i in range(depth + 1):
#     f += xx**i
# print(f)
# bfactor = solve(f)
# print(bfactor)