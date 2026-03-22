from itertools import combinations
from collections import deque
N, M = map(int, input().split())
wall = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []

for i in range(N):
    for j in range(M):
        if wall[i][j] == 0: 
            empty.append((i, j))
        elif wall[i][j] == 2: 
            virus.append((i, j))
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

for walls in combinations(empty, 3):
    temp = [row[:] for row in wall]
    for x, y in walls: 
        temp[x][y] = 1
        
    queue = deque(virus)
    while queue: 
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))
        
    safe_cnt = 0 
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0: 
                safe_cnt += 1
    answer = max(answer, safe_cnt)
print(answer) 