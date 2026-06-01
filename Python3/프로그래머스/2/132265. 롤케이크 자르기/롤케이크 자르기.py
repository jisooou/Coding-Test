def solution(topping):
    right = {}
    for t in topping:
        if t not in right:
            right[t] = 1
        else:
            right[t] += 1
            
    cnt = 0
    left = set()
    for t in topping:
        left.add(t)
        right[t] -= 1
        if right[t] == 0:
            del right[t]
        
        if len(left) == len(right):
            cnt += 1
    return cnt