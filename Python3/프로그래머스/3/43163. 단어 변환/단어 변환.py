from collections import deque
def solution(begin, target, words):
    visited = [False]*len(words)
    queue = deque()
    queue.append((begin, 0))
    
    if target not in words:
        return 0
    
    while queue:
        current_word, cnt = queue.popleft()
        if current_word == target:
            return cnt
        
        for i in range(len(words)):
            new_word = words[i]
            diff = 0
            for j in range(len(begin)):
                if new_word[j] != current_word[j]: 
                    diff += 1
            if not visited[i] and diff==1:
                visited[i] = True
                queue.append((new_word, cnt+1))
    return 0