import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
path = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

INF = float('inf')
answer = INF

# 치킨집과 집을 뽑아내야 됨
for i in range(n):
    for j in range(n):
        if path[i][j] == 1: 
            house.append((i, j))
        elif path[i][j] == 2: 
            chicken.append((i, j))

# 치킨집 중 m만큼 고르기 
for chk in combinations(chicken, m):
    #치킨집 m개 중 1개로 돌 때마다 
    total = 0
    
    #현재 선택된 치킨의 조합 
    for hx, hy in house:
        min_dist = INF
        for cx, cy in chk: 
            #집마다 치킨집과의 거리 계산 
            dist = abs(hx - cx) + abs(hy - cy)
            min_dist = min(min_dist, dist) 
        total += min_dist
    answer = min(answer, total)
print(answer)