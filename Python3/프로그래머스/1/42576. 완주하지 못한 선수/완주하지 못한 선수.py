from collections import Counter
def solution(participant, completion):
    ans = Counter(participant) - Counter(completion) 
    for k in ans:
        return k
    