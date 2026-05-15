def solution(want, number, discount):
    answer = 0
    give_dict = {}
    for i in range(len(want)):
        give_dict[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        have_dict = {}
        for d in discount[i:i+10]:
            if d in have_dict:
                have_dict[d] += 1
            else:
                have_dict[d] = 1
        if give_dict == have_dict:
            answer += 1
            
    return answer