class Square:
    num = 0
    possibleNums = []
    def __init__(self, groupNum, row, col):
        self.groupNum = groupNum
        self.row = row
        self.col = col

userInputBoard = [8,0,0,0,0,0,0,0,0,0,1,3,8,6,7,5,4,9,4,7,0,5,0,3,2,6,0,0,0,0,0,5,0,9,8,1,0,6,8,9,0,0,0,0,0,7,0,1,3,4,0,0,2,0,6,0,0,0,7,0,0,0,4,0,0,7,0,0,9,0,0,0,0,3,0,0,8,0,0,1,2]
board = []

#Pops the whole board array a remakes the board with numbers equal to 0 and sets there row, column, and group information
def resetBoard():
    i=0
    while(i<len(board)):
        board.pop
        i+=1

    for nums in board:
        nums.pop
    i=0
    groupBaseNum = 1
    setRow = 0
    setCol = 0
    setGroup = 1
    while i < 81:
        if(i!=0 and i%9==0):
            setRow +=1
            setCol = 0
        if(setRow>2 and setRow<6):
            groupBaseNum=4
        if(setRow>5):
            groupBaseNum=7
        if(setCol<3):
            setGroup = groupBaseNum
        if(setCol>2 and setCol<6):
            setGroup = groupBaseNum+1
        if(setCol>5):
            setGroup = groupBaseNum+2

        board.append(Square(setGroup,setRow, setCol))
        i+=1
        setCol+=1

#Prints the board to terminal
def printBoard():
    i=0
    int=0
    while i<9:
        print(f'\n')
        print(f'| ', end = '')
        i+=1
        j=0
        while j<9:
            number = str(board[int].num)
            print(f'{number} | ', end = '')
            j+=1
            int+=1

#Sets the board with numbers, runs reset board
def setBoard():
    resetBoard()
    i=0
    while(i<81):
        board[i].num = userInputBoard[i]
        i+=1

#This function goes through and updates all the possibleNums[] the square is allowed to be
def updatePossibilities():
    i=0
    while(i<81):
        if(board[i].num==0):
            allNums = [1,2,3,4,5,6,7,8,9]
            j=0
            while(j<81):
                if(board[j].num!=0):
                    if((board[j].row == board[i].row) or (board[j].col == board[i].col) or (board[j].groupNum == board[i].groupNum)):
                        for nums in allNums:
                            if(board[j].num == nums):
                                allNums.remove(nums)
                j+=1
            board[i].possibleNums = allNums[:]
        i+=1

#Checks all the numbers to see if a box can only be one possible number, restarts the check if a number is changed
#and re-runs the updatePossibilities to refresh possibleNums[]
def checkForSolo():
    i=0
    while(i<81):
        hasChanged = False
        if(len(board[i].possibleNums)==1):
            board[i].num = board[i].possibleNums[0]
            board[i].possibleNums.pop()
            hasChanged = True
            updatePossibilities()
        if(hasChanged):
            i=0
        else:
            i+=1

#Takes the current elements possibleNums[] and compares it to the other elements possibleNums[]. If this has a unique
#number, it sets that square to that number and re-runs updatePossibilities to refresh possibleNums[]
def checkForHasToBe():
    i=0
    didChange = False
    while(i<81):
        checkPosNums = []
        checkPosNums = board[i].possibleNums[:]
        j=0
        while(j<0):
            if(board[j].row == board[i].row) or (board[j].col == board[i].col) or (board[j].groupNum == board[i].groupNum):
                for checkPosNum in checkPosNums:
                    for curNum in board[j].possibleNums:
                        if(checkPosNum == curNum):
                            checkPosNums.remove(checkPosNum)
            j+=1
        if(len(checkPosNums)==1):
            board[i].num = checkPosNums[0]
            board[i].possibleNums.clear()
            updatePossibilities()
            didChange = True
        if(didChange):
            i=0
        else:
            i+=1

#Makes one guess and then revaluates the board. Anything not done yet it will guess again
def bruteForce():
    for squares in board:
        if(squares.num == 0):
            squares.num = squares.possibleNums[0]
            solve()

#Runs updatePossibilities, then checkForSolo, then checkForHasToBe, then bruteForce, then lastly it will print
def solve():
    updatePossibilities()
    checkForSolo()
    checkForHasToBe()
    bruteForce()
    print(f'\n')
    printBoard()

setBoard()
solve()
