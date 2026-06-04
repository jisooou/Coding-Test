from collections import deque
def solution(priorities, location):
    queue = deque()
    for idx, value in enumerate(priorities):
        queue.append((idx, value))
    
    cnt = 0
    while queue:
        pop_idx, pop_value = queue.popleft()
        for i, v in queue:
            if pop_value < v:
                queue.append((pop_idx, pop_value))
                break
        else:
            cnt += 1
            if pop_idx == location:
                return cnt