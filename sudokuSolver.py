class Square:
    num = 0
    possibleNums = []
    def __init__(self, groupNum, row, col):
        self.groupNum = groupNum
        self.row = row
        self.col = col

board = []

#Resets the board with numbers equal to 0
def resetBoard():
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
            print(f'{board[int].num} | ', end = '')
            j+=1
            int+=1

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
    hasChanged = False
    i=0
    while(i<81):
        if(len(board[i].possibleNums)==1):
            board[i].num = board[i].possibleNums[0]
            board[i].possibleNums.pop()
            hasChanged = True
            updatePossibilities()
        if(hasChanged):
            i=0
        else:
            i+=1

def checkForHasToBe():
    return ("hi")

resetBoard()
printBoard()