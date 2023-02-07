class PuzzleBoard:
    def __init__(self, state, pathCost):
        self.state = state
        self.pathCost = pathCost
        
        
    # heuristic 1: number of misplaced tiles
    def h1(self):
        curWrong = 0
        for i in range(1, 9):
            if self.state.index(i) != i:
                curWrong += 1
        return curWrong
    
    
    # heuristic 2: city block distance 
    def h2(self, path=0):
        totalSteps = 0
        
        for i in range(1, 9):
            curIndex = self.state.index(i)
            # takes care of wrapping around board right 
            # to left from 2 or 5
            while (curIndex == 2 or curIndex == 5) and (curIndex < i):
                curIndex += 3
                totalSteps += 1
            # takes care of wrapping around board left 
            # to right from 3 or 6
            while (curIndex == 3 or curIndex == 6) and (curIndex > i):
                curIndex += 3
                totalSteps += 1
            
            if curIndex > i:
                while (curIndex - 3) > i:
                    curIndex -= 3
                    totalSteps += 1
                while (curIndex - 1) >= i:
                    curIndex -= 1
                    totalSteps += 1
            elif curIndex < i:
                while (curIndex + 3) < i:
                    curIndex += 3
                    totalSteps += 1
                while (curIndex + 1) <= i:
                    curIndex += 1
                    totalSteps += 1
        return totalSteps
    
    
    # this helper returns a list that represents the next state
    def nextStateHelper(self, curIndex, tempState, indexChange):
        tempState = self.state.copy()
        nextIndex = curIndex + indexChange
        movedValue = self.state[nextIndex]
        tempState[nextIndex] = 0
        tempState[curIndex] = movedValue
        return tempState
    
    def getNextStates(self):
        # curIndex is the index of 0 which represents the blank tile
        curIndex = self.state.index(0)
        nextStates = []
        copyState = self.state.copy()
        # makes sure up is a legal move
        if not (curIndex < 3):
            tempState = self.nextStateHelper(curIndex, copyState, (-3))
            nextStates.append(PuzzleBoard(tempState, self.pathCost + 1))
        # makes sure down is a legal move
        if not (curIndex > 5):
            tempState = self.nextStateHelper(curIndex, copyState, 3)
            nextStates.append(PuzzleBoard(tempState, self.pathCost + 1))
        # makes sure left is a legal move 
        if not (curIndex == 0 or curIndex == 3 or curIndex == 6):
            tempState = self.nextStateHelper(curIndex, copyState, -1)
            nextStates.append(PuzzleBoard(tempState, self.pathCost + 1))
        # makes sure right is a legal move 
        if not (curIndex == 2 or curIndex == 5 or curIndex == 8):
            tempState = self.nextStateHelper(curIndex, copyState, 1)
            nextStates.append(PuzzleBoard(tempState, self.pathCost + 1))
        return nextStates
            
    
    def solvable(self):
        count = 0
        tempState = self.state.copy()
        tempState.remove(0)
        for i in range(len(tempState) - 1):
            for j in tempState[i:]:
                if j < tempState[i]:
                    count+=1
        if count%2 != 0:
            return False 
        else:
            return True 
    
    def __str__(self):
        return f"{self.state[:3]}\n{self.state[3:6]}\n{self.state[6:9]}"