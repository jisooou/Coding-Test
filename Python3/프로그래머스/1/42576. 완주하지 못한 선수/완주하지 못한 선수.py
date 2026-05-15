from collections import Counter
def solution(participant, completion):
    ans = Counter(participant) - Counter(completion) 
    return list(ans.keys())[0]
    # for k in ans:
    #     return k