from queue import PriorityQueue
from puzzleboard import PuzzleBoard
from AStar import AStar
from generateRandomPuzzle import batchPuzzles
from tabulate import tabulate 
from ids import IDS

# goal state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

h1 = batchPuzzles(1200, 'h1') 
h2 = batchPuzzles(1200, 'h2')
ids = batchPuzzles(600, 'ids')

h1data = []
h2data = []
idsdata = []
for i in range(2, 25, 2):
    try:
        h1data.append([i, sum(h1[i]) / len(h1[i]), len(h1[i])])
    except:
        h1data.append([i, 'na', 0])
    try:
        h2data.append([i, sum(h2[i]) / len(h2[i]), len(h2[i])])
    except:
        h2data.append([i, 'na', 0])
for i in range(2, 13, 2):
    try:
        idsdata.append([i, sum(ids[i]) / len(ids[i]), len(ids[i])])
    except:
        idsdata.append([i, 'na', 0])
h1colHeaders = ['d', 'A*(h1)', 'total h1']
h2colHeaders = ['d', 'A*(h2)', 'total h2']
idscolHeaders = ['d', 'IDS', 'total ids']
with open("newFile.txt", 'a') as f:
    f.write(str(tabulate(h1data, headers=h1colHeaders, tablefmt='simple')) + "\n")
    f.write(str(tabulate(h2data, headers=h2colHeaders, tablefmt='simple')) + "\n")
    f.write(str(tabulate(idsdata, headers=idscolHeaders, tablefmt='simple')) + "\n")
print(tabulate(h1data, headers=h1colHeaders, tablefmt='simple'))
print()
print(tabulate(h2data, headers=h2colHeaders, tablefmt='simple'))
print()
print(tabulate(idsdata, headers=idscolHeaders, tablefmt='simple'))
