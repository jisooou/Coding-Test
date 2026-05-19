def solution(keymap, targets):
    answer = []
#     각 알파벳이 최소 몇번 눌러야하는지 
    press_alpha = {}
    for k in keymap:
        for idx, ch in enumerate(k):
            press = idx+1
            if ch not in press_alpha:
                press_alpha[ch] = press
            else:
                press_alpha[ch] = min(press_alpha[ch], press)
                
    for t in targets:
        total = 0
        for ch in t: 
            if ch not in press_alpha:
                total = -1
                break
            total += press_alpha[ch]
        answer.append(total)
    return answer