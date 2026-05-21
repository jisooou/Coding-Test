def solution(keymap, targets):
    answer = []
    alpha = {}
    for k in keymap:
        for idx, word in enumerate(k):
            press = idx + 1
            if word in alpha:
                alpha[word] = min(alpha[word], press)
            else:
                alpha[word] = press
    
    for t in targets:
        total = 0
        for target_word in t:
            if target_word not in alpha:
                total = -1
                break
            total += alpha[target_word]
        answer.append(total)
    return answer    