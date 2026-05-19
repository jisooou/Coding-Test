def solution(answers):
    answer = []
    idx_one = [1, 2, 3, 4, 5]
    idx_two = [2, 1, 2, 3, 2, 4, 2, 5]
    idx_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for idx, a in enumerate(answers):
        if a == idx_one[idx%len(idx_one)]:
            score[0] += 1
        if a == idx_two[idx%len(idx_two)]:
            score[1] += 1
        if a == idx_three[idx%len(idx_three)]:
            score[2] += 1
        #score[5,7,7]    
    
    max_score = max(score)
    for i in range(3):
        if score[i] == max_score:
            answer.append(i+1)
    return answer
        