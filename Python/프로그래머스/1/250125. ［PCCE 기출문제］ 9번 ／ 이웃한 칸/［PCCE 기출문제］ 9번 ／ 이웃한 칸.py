def solution(board, h, w):
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    cnt = 0
    target = board[h][w]
    board_len = len(board)
    
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        if 0 <= nx < board_len and 0 <= ny < board_len:
            if target == board[nx][ny]:
                cnt += 1
                
    return cnt