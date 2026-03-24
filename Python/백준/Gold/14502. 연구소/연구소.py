from collections import deque
from itertools import combinations

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

zero = []
virus = []

for i in range(N):
    for j in range(M):
        if data[i][j] == 0: 
            zero.append((i,j))
        elif data[i][j] == 2: 
            virus.append((i,j))

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
            
for walls in combinations(zero, 3):
    # 배열을 복사해 준다. 
    temp = [row[:] for row in data]
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