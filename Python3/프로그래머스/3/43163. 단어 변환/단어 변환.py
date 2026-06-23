from collections import deque
def solution(begin, target, words):
    queue = deque()
    queue.append((begin, 0))
    visited = [False] * len(words)
    
    if target not in words:
        return 0
    
    while queue:
        word, cnt = queue.popleft()
        if word == target:
            return cnt 
        
        for nxt_word in range(len(words)): 
            diff = 0
            for i in range(len(word)):
                if word[i] != words[nxt_word][i]:
                    diff += 1
            if diff == 1 and not visited[nxt_word]:
                visited[nxt_word] = True
                queue.append((words[nxt_word], cnt+1))
        
   