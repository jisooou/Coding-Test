def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for idx, i in enumerate(answers):
        if i == first[idx%len(first)]:
            score[0] += 1
        if i == second[idx%len(second)]:
            score[1] += 1
        if i == third[idx%len(third)]:
            score[2] += 1

    result = []
    max_score = max(score)
    for i in range(len(score)):
        if score[i] == max_score:
            result.append(i+1)
    return result