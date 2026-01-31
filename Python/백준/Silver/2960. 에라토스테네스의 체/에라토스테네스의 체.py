import sys

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False] * (N+1)
cnt = 0

for i in range(2, N+1):
    if not visited[i]:
        for j in range(i, N+1, i):
            if not visited[j]:
                visited[j] = True
                cnt += 1
                if cnt == K:
                    print(j)