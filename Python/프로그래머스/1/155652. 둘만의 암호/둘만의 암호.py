def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for sk in skip:
        alpha = alpha.replace(sk, '')
    for word in s:
        answer += alpha[(alpha.index(word) + index)%len(alpha)] 
    return answer