def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for n in range(len(number)):
        want_dict[want[n]] = number[n]
    
    for d in range(len(discount)-9):
        have_dict = {}
        for food in discount[d:d+10]:
            if food in have_dict:
                have_dict[food] += 1
            else:
                have_dict[food] = 1
    
        if want_dict == have_dict:
            answer += 1
        
    return answer