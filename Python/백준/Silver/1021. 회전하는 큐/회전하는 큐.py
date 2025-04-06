from collections import deque

n, m = map(int, input().split())
target = list(map(int, input().split()))

dq = deque(range(1, n+1))
count = 0

for t in target: 
    idx = dq.index(t)
    
    if idx == 0:
        dq.popleft()
    elif idx <= len(dq) // 2:
        for _ in range(idx):
            dq.append(dq.popleft())
            count += 1
        dq.popleft()
    else:
        for _ in range(len(dq) - idx):
            dq.appendleft(dq.pop())
            count += 1
        dq.popleft()

print(count)