N, M = map(int, input().split())
J = int(input())
left = 1
right = M
cnt = 0

for _ in range(J): 
    apple = int(input())
    if apple < left: 
        move = left - apple
        cnt += move
        left -= move
        right -= move
    elif apple > right: 
        move = apple - right 
        cnt += move
        left += move
        right += move
        
print(cnt)