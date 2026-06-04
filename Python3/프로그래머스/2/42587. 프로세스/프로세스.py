from collections import deque
def solution(priorities, location):
    queue = deque()
    for idx, p in enumerate(priorities):
        queue.append((idx, p))
    
    cnt = 0
    while queue: 
        p_idx, p_value = queue.popleft()
        for idx, p in queue:
            if p_value < p:
                queue.append((p_idx ,p_value))
                break
        else:
            cnt += 1
            if p_idx == location:
                return cnt