def solution(k, m, score):
    sort_score = sorted(score, reverse=True)
    answer = 0
    for i in range(len(score)//m):
        answer += sort_score[(i+1)*m-1]*m
    return answer
        