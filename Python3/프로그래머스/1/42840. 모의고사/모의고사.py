def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for idx, a in enumerate(answers):
        if a == first[idx%len(first)]:
            score[0] += 1
        if a == second[idx%len(second)]:
            score[1] += 1
        if a == third[idx%len(third)]:
            score[2] += 1
    
    max_score = max(score)
    for s in range(3):
        if score[s] == max_score:
            answer.append(s+1)        
    return answer