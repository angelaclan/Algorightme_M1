#P= blanc
#p= noir

#configuration :

m = int(input('pls enter a number of colonne : '))
n = int(input('pls enter a number of row : '))
l = []

for i in range(0, n):
    str1 = input()
    l.append(str1.split())

value = 1

whitepion = value % 2 = 1
blackpion = value % 2 = 0

# using deepcopy for deepcopy  
def chess(column, row, board, value) :
     
        
    for i in range(0, column) :
        copyboard = copy.deepcopy(board)
        currentpos = copyboard[row+i]
        value = value + i
    return chess(column-1, row-1, board, value)
    
   
#if P == board[n][_] or p in board[n-n][_] :
#if P in board[n][m], p in board[n][m -1]  
    
if __name__=='__main__':
    n = int(input('pls enter a number of colonne : '))
    m = int(input('pls enter a number of row : '))
    l = []
    
   
    for i in range(0, m):
        str1 = input()
        board.append(str1.split())
    print("list:", board)

    print(chess(n, m, P, p))
#if move = eat adversary in diagonale, or move forward
#    if 0<i<colonne && 0<j<row, P move colonne -1; p move colonne +1
#    if P board[i][j] p board[i][j+1] or board[i][j-1] p replace p
    
