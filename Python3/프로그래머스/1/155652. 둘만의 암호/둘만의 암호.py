def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for sk in skip:
        alpha = alpha.replace(sk, '')
    for i in s: 
        idx = (alpha.index(i)+index)%len(alpha)
        answer += alpha[idx]
    return answer