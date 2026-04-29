def solution(answers):
    answer = []
    
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    first_cnt = 0
    second_cnt = 0
    third_cnt = 0
    
    for i in range(len(answers)):
        if answers[i] == first[i%len(first)]:
            first_cnt += 1
        if answers[i] == second[i%len(second)]:
            second_cnt += 1
        if answers[i] == third[i%len(third)]:
            third_cnt += 1
            
    score = [first_cnt, second_cnt, third_cnt]
    
    for s in range(len(score)):
        if score[s] == max(score):
            answer.append(s+1)
    return answer