import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    scope = [(x, y)]
    total = board[x][y]
    
    while queue: 
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(board[x][y] - board[nx][ny]) <= R:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    scope.append((nx, ny))
                    total += board[nx][ny]
    return scope, total    

day = 0
    
while True: 
    visited = [[False] * N for _ in range(N)]
    move = False 
   
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                scope, total = bfs(i, j)
                
                if len(scope) > 1:
                    move = True
                    new_move = total // len(scope)
                    for x, y in scope: 
                        board[x][y] = new_move
    if not move: 
        break 
        
    day += 1
print(day)