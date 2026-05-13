def solution(babbling):
    answer = 0
    words = ['aya', 'ye', 'woo', 'ma']
    for b in babbling:
        for w in words:
            if w*2 in b:
                break
            b = b.replace(w, ' ')
        if b.strip() == '':
            answer += 1
    return answer