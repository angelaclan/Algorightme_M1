import copy
whitePawnSymbol = 'P'
blackPawnSymbol = 'p'
spaceSymbol = ' '


def getSuccessors(config) :
    boardCopy = copy.deepcopy(config[0])
    player = config[1]
    direction = -1 if (player==whitePawnSymbol) else 1
    indexBlackArea= 0
    indexWhiteArea = len(boardCopy)-1
    
    successors = list()
    
    for line in boardCopy :
        lineIndex = boardCopy.index(line)
        otherPlayer = blackPawnSymbol  if (player==whitePawnSymbol ) else whitePawnSymbol 
        
        if lineIndex == indexBlackArea and whitePawnSymbol in line or lineIndex == indexWhiteArea and blackPawnSymbol in line:
            return []
        
        for columnIndex in range(len(line)):
            if line[columnIndex] == player:                
                # On regarde une case en avant dans une direction, si la case est vide on avance pion du joueur
                if lineIndex+direction >= 0 and lineIndex+direction < len(boardCopy):
                    if boardCopy[lineIndex+direction][columnIndex] == spaceSymbol :
                        successorBoard = copy.deepcopy(boardCopy)
                        successorBoard[lineIndex+direction][columnIndex] = player
                        successorBoard[lineIndex][columnIndex] = spaceSymbol
                        successors.append( [successorBoard, otherPlayer])
                    
                    # On regarde si on peut capturer un pion adverse en diagonal
                    if columnIndex-1 >= 0 and boardCopy[lineIndex+direction][columnIndex-1] == otherPlayer :
                        successorBoard = copy.deepcopy(boardCopy)
                        successorBoard[lineIndex+direction][columnIndex-1] = player
                        successorBoard[lineIndex][columnIndex] = spaceSymbol
                        successors.append( [successorBoard, otherPlayer])
                        
                    if columnIndex+1 < len(line) and boardCopy[lineIndex+direction][columnIndex+1] == otherPlayer :
                        successorBoard = copy.deepcopy(boardCopy)
                        successorBoard[lineIndex+direction][columnIndex+1] = player
                        successorBoard[lineIndex][columnIndex] = spaceSymbol
                        successors.append( [successorBoard, otherPlayer])
    
    return successors

def allPositive(l):
    for e in l:
        if e < 0:
            return False
    return True

def extractNegativeValues(values):
    negativeValues = list()
    for v in values:
        if v < 0 :
            negativeValues.append(v)
            
    return negativeValues

