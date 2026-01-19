import sys
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
answer = float('inf')

def dfs(idx, cnt):
    global answer

    # 팀이 N/2명 찼으면 능력치 계산
    if cnt == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += data[i][j]
                elif not visited[i] and not visited[j]:
                    link += data[i][j]
        answer = min(answer, abs(start - link))
        return

    # 조합 생성
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, cnt + 1)
            visited[i] = False

dfs(0, 0)
print(answer)