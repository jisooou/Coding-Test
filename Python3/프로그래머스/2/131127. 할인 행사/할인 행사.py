def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        current = {}
        for item in discount[i:i+10]:
            if item in current: 
                current[item] += 1
            else:
                current[item] = 1
        
        if current == want_dict:
            answer += 1
        
    return answer