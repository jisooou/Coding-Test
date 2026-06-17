from collections import Counter
def solution(participant, completion):
    remain = Counter(participant) - Counter(completion)
    for i in remain.keys():
        return i