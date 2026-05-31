def solution(topping):
    cnt = 0
    right = {}
    for element in topping:
        if element not in right:
            right[element] = 1
        else:
            right[element] += 1
    
    left = set()
    for element in topping:
        left.add(element)
        right[element] -= 1
        if right[element] == 0:
            del right[element]
        
        if len(left) == len(right):
            cnt += 1
    return cnt