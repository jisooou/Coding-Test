from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    
    queue = deque()
    queue.append((begin, 0))
    while queue:
        word, cnt = queue.popleft()
        if word == target:
            return cnt
        
        for i in range(len(words)):
            nxt_word = words[i]
            diff = 0
            for j in range(len(word)):
                if word[j] != nxt_word[j]:
                    diff += 1
            if not visited[i] and diff == 1:
                visited[i] = True
                queue.append((nxt_word, cnt+1))
    return 0