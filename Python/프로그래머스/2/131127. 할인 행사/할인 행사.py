def solution(want, number, discount):
    answer = 0
    have_dict = {}
    for w in range(len(want)):
        have_dict[want[w]] = number[w]
    for d in range(len(discount)-9):
        want_dict = {}
        for idx in discount[d:d+10]:
            if idx in want_dict:
                want_dict[idx] += 1
            else:
                want_dict[idx] = 1
        
        if have_dict == want_dict:
            answer += 1
    return answer