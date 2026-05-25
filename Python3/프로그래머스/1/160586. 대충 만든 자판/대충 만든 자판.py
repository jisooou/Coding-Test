def solution(keymap, targets):
    alpha_find = {}
    for k in keymap:
        for idx, alpha in enumerate(k):
            press = idx + 1
            if alpha not in alpha_find:
                alpha_find[alpha] = press
            else:
                alpha_find[alpha] = min(press, alpha_find[alpha])
    
    answer = []
    for t in targets:
        total = 0
        for target in t:
            if target not in alpha_find:
                total = -1
                break
            else:
                total += alpha_find[target]
        answer.append(total)
    return answer
            