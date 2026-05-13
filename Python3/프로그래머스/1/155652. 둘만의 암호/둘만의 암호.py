def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        alpha = alpha.replace(i, '')
    for word in s:
        idx = (alpha.index(word)+index)%len(alpha)
        answer += alpha[idx]
    return answer