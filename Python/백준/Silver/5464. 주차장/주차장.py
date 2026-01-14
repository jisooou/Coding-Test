import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

cost = [int(input()) for _ in range(N)]
weight = [0] + [int(input()) for _ in range(M)]

parking = [0] * N
car_pos = [0] * (M + 1)
wait = deque()

total = 0

for _ in range(2 * M):
    x = int(input())

    if x > 0:  
        parked = False
        for i in range(N):
            if parking[i] == 0:
                parking[i] = x
                car_pos[x] = i
                total += cost[i] * weight[x]
                parked = True
                break
        if not parked:
            wait.append(x)

    else:  
        car = -x
        pos = car_pos[car]
        parking[pos] = 0

        if wait:
            next_car = wait.popleft()
            parking[pos] = next_car
            car_pos[next_car] = pos
            total += cost[pos] * weight[next_car]

print(total)