def solution(board):
    row = len(board)
    column = len(board[0])
    answer = 0
    
    for x in range(row):
        for y in range(column):
            if board[x][y] == 1:
                if x==0 or y==0:
                    answer = max(answer, 1)
                else:
                    board[x][y] = min(
                        board[x-1][y],
                        board[x][y-1],
                        board[x-1][y-1]
                    )+1
                    answer = max(answer, board[x][y])
    return answer*answer