import sys
from collections import deque 

q = deque()
stack = [] #최근 추가된 걸 pop하기 위해서 위치를 알기 위함이다.
input = sys.stdin.readline
N = int(input()) # 5 
for _ in range(N):
    command = input().strip().split() #리스트로 넣어준다 
    if command[0] == '1':
        c = command[1]
        q.append(c)
        stack.append(('back', c))
    elif command[0] == '2':
        c = command[1]
        q.appendleft(c)
        stack.append(('front', c))
    elif command[0] == '3':
        if not stack:
            continue
        position, k = stack.pop()
        if position == 'back' and q and q[-1] == k:
            q.pop()
        elif position == 'front' and q and q[0] == k:
            q.popleft()
if q: 
    print("".join(q))
else:
    print(0)
