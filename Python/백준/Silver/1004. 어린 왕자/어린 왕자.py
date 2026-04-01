import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    sx, sy, ex, ey = map(int, input().split())
    star_cnt = int(input())
    cnt = 0
    for _ in range(star_cnt):
        cx, cy, r = map(int, input().split())
        
        start_in = (sx-cx)**2 + (sy-cy)**2 < r**2
        end_in = (ex-cx)**2 + (ey-cy)**2 < r**2
        
        if start_in != end_in: 
            cnt += 1
    print(cnt)    