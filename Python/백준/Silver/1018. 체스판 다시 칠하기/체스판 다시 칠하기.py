import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

answer = 64 # 최대 8*8

for x in range(n-7):
    for y in range(m-7):
        white_start = 0
        black_start = 0
        
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j)%2 == 0:
                    if board[i][j] != 'W':
                        white_start += 1
                    if board[i][j] != 'B':
                        black_start += 1
                else: 
                    if board[i][j] != 'B':
                        white_start += 1
                    if board[i][j] != 'W':
                        black_start += 1

        answer = min(answer, white_start, black_start)
print(answer)