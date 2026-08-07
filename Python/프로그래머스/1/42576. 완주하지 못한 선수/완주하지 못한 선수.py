from collections import Counter
def solution(participant, completion):
    #동명이인 처리 
    partici_count = Counter(participant) #{'mislav':2, 'stanko':1...}
    comple_count = Counter(completion)
    remain = partici_count - comple_count
    return list(remain.keys())[0]