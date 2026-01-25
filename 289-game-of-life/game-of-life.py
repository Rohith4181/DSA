class Solution(object):
    def gameOfLife(self, board):

        m,n = len(board), len(board[0])

        newBoard = [[0]*n for _ in range(m)]

        for i in range(0,m):
            for j in range(0,n):

                cell = board[i][j]
                live = 0

                if(i+1 < m):
                    if(board[i+1][j] == 1):
                        live += 1 

                if(j+1 < n):
                    if(board[i][j+1] == 1):
                        live += 1 


                if(i-1 >=0):
                    if(board[i-1][j] == 1):
                        live += 1  

                if(j-1 >= 0):
                    if(board[i][j-1] == 1):
                        live += 1 
                

                if(i+1 < m and j -1 >= 0):
                    if(board[i+1][j-1] == 1):
                        live += 1 

                if(i+1 < m and j+1 < n):
                    if(board[i+1][j+1] == 1):
                        live += 1

                if(i-1 >=0 and j -1 >= 0):
                    if(board[i-1][j-1] == 1):
                        live += 1

                if(i-1 >=0 and j + 1 < n):
                    if(board[i-1][j+1] == 1):
                        live += 1

                if(cell == 1):
                    if(live < 2 or live > 3):
                        newBoard[i][j] = 0
                    else:
                        newBoard[i][j] = 1
                elif(cell == 0):
                    if(live == 3):
                        newBoard[i][j] = 1

        for i in range(0,m):
            for j in range(0,n):
                board[i][j] = newBoard[i][j]