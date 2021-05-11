k = 0
boards = [[[0 for i in range(8)]for j in range(8)]for k in range(92)]
def printSolution(board):
    global k
    for i in range(8):
        for j in range(8):
            boards[k][i][j] = board[i][j]
    k += 1
def isSafe(board, row, col):
    for i in range(col):
        if (board[row][i]):
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if (board[i][j]):
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while j >= 0 and i < 8:
        if (board[i][j]):
            return False
        i = i + 1
        j = j - 1

    return True
def solveNQUtil(board, col):
    if (col == 8):
        printSolution(board)
        return True
    res = False
    for i in range(8):
        if (isSafe(board, i, col)):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0

    return res
def solveNQ():
    board = [[0 for j in range(8)]
             for i in range(8)]
    if (solveNQUtil(board, 0) == False):
        print("Solution does not exist")
        return
    return
solveNQ()
req = []
res = 0
x = [list(input()) for i in range(8)]
for i in range(8):
    for j in range(8):
        if x[i][j] == "*":
            req.append([i, j])
for k in range(92):
    for x, y in req:
        if boards[k][x][y] == 1:
            res += 1
            break
print(92-res)

