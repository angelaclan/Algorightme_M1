from copy import deepcopy


def loadBoardFromInput (): 
    rows = int(input(''))
    cols = int(input(''))
    board = [[None for col in range(cols)] for row in range(rows)]
    for i in range (rows):
        lineDef = input ('')
        for j in range (len(lineDef)):
            print (lineDef[j])
            if not lineDef[j].isspace():
                board[i][j] = lineDef[j]
    return board

def printBoards (boards) :
    for b in boards :
        printBoard(b)
        print ('')

def printBoard (board) :
    for row in board:
        line = ''
        for col in row:
            if col is None:
                line = line + '_'
            elif col == 'P':
                line = line + 'X'
            else:
                line = line + 'O'
        print (line)
  

def somebodyWon (board):
  
    if 'P' in board[0]:
        return True
    if 'p' in board[-1]:
        return True

    return False
    
def canMoveUp(board,pawn):
    x = pawn[0]
    y = pawn[1]
    if not board[x][y] == 'P':
        return False
    if x == 0:
        return False
    return board[x - 1][y] is None

def canMoveDown(board,pawn):
    x = pawn[0]
    y = pawn[1]
    if not board[x][y] == 'p':
        return False
    if x == len(board) -1:
        return False
    return board[x + 1][y] is None

def canMoveDownDiagonalPlus(board,pawn):
    x = pawn[0]
    y = pawn[1]
    if not board[x][y] == 'p':
        return False
    if x == len(board) -1:
        return False
    if y == len(board[x]) -1:
        return False
    return board[x + 1][y + 1] == 'P'

def canMoveDownDiagonalMinus(board,pawn):
    x = pawn[0]
    y = pawn[1]
    if not board[x][y] == 'p':
        return False
    if x == len(board) -1:
        return False
    if y == 0:
        return False
    return board[x + 1][y - 1] == 'P'
    
def canMoveUpDiagonalPlus(board,pawn):
    x = pawn[0]
    y = pawn[1]
    if not board[x][y] == 'P':
        return False
    if x == len(board) -1:
        return False
    if y == len(board[x]) - 1:
        return False
    return board[x - 1][y + 1] == 'p'

def canMoveUpDiagonalMinus(board,pawn):
    x = pawn[0]
    y = pawn[1]
    if not board[x][y] == 'P':
        return False
    if x == len(board) - 1:
        return False
    if y == 0:
        return False
    return board[x - 1][y - 1] == 'p'

def boardcopyWith (board, origin, destination) :
    newBoard = deepcopy(board)
    
    x = origin[0]
    y = origin[1]
    
    value = newBoard[x][y]
    newBoard[x][y] = None
    
    xDest = destination[0]
    yDest = destination[1]
    
    newBoard[xDest][yDest] = value
    
    return newBoard

''' ****************************************************************************************************************
    Following some improvised test cases 7. 8.
    **************************************************************************************************************** '''
#board = [  [None, None, None, None, None, None],  ['p', 'p', None, 'p', 'p', None],  ['P', None, 'p', None, None, 'P'], [None, 'P', 'P', 'P', None, 'p'], [None, None, None, None, 'P', None],  [None, None, None, None, None, None] ]
# assert (canMoveDown(board,(1,0) ) is False)
# assert (canMoveDown(board,(1,4) ) is True)
# assert (canMoveUp(board,(2,2) ) is False)
# assert (canMoveUp(board,(3,1) ) is True)
# assert (canMoveDown(board,(3,1) ) is False)
# assert (canMoveUpDiagonalMinus(board,(3,1) ) is False)
# assert (canMoveUpDiagonalPlus(board,(3,1) ) is True)
# board = [ [None, None, None, None, None, None], ['p', None, 'p', None, 'p', None], ['P', 'p', None, None, 'P', None], [None, None, None, None, None, None], ['P', 'P', 'P', None, 'p', None], [None, None, None, None, 'P', None] ]
#board = [[None, 'p', None, 'p'], ['p', 'P', 'P', None], ['P', None, None, 'P']]
#board = [[None, 'p', None, 'p'], ['p', 'P', None, None], [None, None, 'P', 'P']]
board = [['p', None, 'p', 'p'], [None, 'p', None, None], ['P', 'P', None, None], [None, None, 'P', 'P']]
''' ****************************************************************************************************************
    End Testing
    **************************************************************************************************************** ''' 
# b pawn
def pPlayerPlays (board) :
    
    if somebodyWon(board):
        printBoard(board)
        return (True, 0, 1)    
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if canMoveDown(board, (i,j)) :
                tuple = PPlayerPlays(boardcopyWith (board, (i,j), (i+1, j)))
                if tuple[0] :
                    return (tuple[0], tuple[1], tuple[2]+1)
            if canMoveDownDiagonalPlus(board, (i,j)) :
                tuple = PPlayerPlays(boardcopyWith (board, (i,j), (i+1, j+1)))
                if tuple[0] :
                    return (tuple[0], tuple[1], tuple[2]+1)            
                
            if canMoveDownDiagonalMinus(board, (i,j)) :
                tuple = PPlayerPlays(boardcopyWith (board, (i,j), (i+1, j-1)))
                if tuple[0] :
                    return (tuple[0], tuple[1], tuple[2]+1)

    return somebodyWon(board)

# w pawn
def PPlayerPlays (board) :
    
    if somebodyWon(board):
        printBoard(board)
        return (True, 1, 0)
          
    for i in range(len(board)):
        for j in range(len(board[i])):
            if canMoveUp(board, (i,j)) :
                tuple = pPlayerPlays(boardcopyWith (board, (i,j), (i-1, j)))
                if tuple[0]:
                    return (tuple[0], tuple[1]+1, tuple[2])
                    
            if canMoveUpDiagonalPlus(board, (i,j)) :
                tuple = pPlayerPlays(boardcopyWith (board, (i,j), (i-1, j+1)))
                if tuple[0]:
                    return (tuple[0], tuple[1]+1, tuple[2])
            if canMoveUpDiagonalMinus(board, (i,j)) :
                tuple = pPlayerPlays(boardcopyWith (board, (i,j), (i-1, j-1)))
                if tuple[0]:
                    return(tuple[0], tuple[1]+1, tuple[2])
               
    return somebodyWon(board)

pos = PPlayerPlays(board)
print(pos[1])


# def sizeList (l) :
#     if len (l) == 0 : return 0
#     return 1 + sizeList(l[1:])
