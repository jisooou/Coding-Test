import sys
input = sys.stdin.readline

N = int(input()) # 3
cnt = 0

for _ in range(N):
    M = input().strip()
    stack = []
    is_group = True
    
    for ch in M: 
        if not stack: 
            stack.append(ch)
        else: 
            if stack[-1] == ch: 
                continue
            elif ch in stack:
                is_group = False
                break 
            else: 
                stack.append(ch)

    if is_group: 
        cnt += 1 
        
print(cnt)