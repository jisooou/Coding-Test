from collections import Counter
def solution(participant, completion):
    remain = Counter(participant) - Counter(completion)
    for answer in remain:
        return answer