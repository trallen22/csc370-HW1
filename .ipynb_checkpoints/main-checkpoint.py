from queue import PriorityQueue
from puzzleboard import PuzzleBoard
from AStar import AStarH1, AStarH2

# goal state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

initialState = [3, 2, 5,
                4, 0, 1,
                6, 7, 8]

b = PuzzleBoard(initialState, 0)

print("INITIAL STATES: ")
print(b)


print(AStarH1(b))

print(AStarH2(b))