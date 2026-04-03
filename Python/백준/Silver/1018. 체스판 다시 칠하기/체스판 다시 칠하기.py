import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
answer = 64 # 8*8

for x in range(n-7):
    for y in range(m-7):
        white_b = 0
        black_b = 0
        
        for i in range(x, x+8):
            for j in range(y, y+8):
                if ((i+j) % 2 == 0): 
                    if board[i][j] != 'W':
                        white_b += 1
                    if board[i][j] != 'B':
                        black_b += 1
                else: 
                    if board[i][j] != 'W':
                        black_b += 1
                    if board[i][j] != 'B':
                        white_b += 1
        answer = min(answer, black_b, white_b)
print(answer)                    