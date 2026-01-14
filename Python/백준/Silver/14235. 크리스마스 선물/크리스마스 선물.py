import sys
import heapq

input = sys.stdin.readline

n = int(input())
qp = []

for _ in range(n):
    data = list(map(int, input().split()))
    if (data[0]==0):
        if qp:
            print(-(heapq.heappop(qp)))
        else: 
            print(-1)
    else:
        for x in data[1:]:
            heapq.heappush(qp, -x)