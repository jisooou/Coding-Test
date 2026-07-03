def solution(citations):
    citations.sort()
    #[0 1 3 5 6]
    answer = 0
    for idx, i in enumerate(citations):
        h_idx = min(i, len(citations)-idx) 
        answer = max(answer, h_idx)
    return answer