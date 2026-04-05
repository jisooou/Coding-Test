import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

answer = 1

for i in range(n):
    for j in range(m):
        for k in range(min(n-i, m-j)):
            if board[i][j] == board[i][j+k] == board[i+k][j] == board[i+k][j+k]:
                answer = max(answer, (k+1)**2)
print(answer)