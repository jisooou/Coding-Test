def solution(s, n):
    #ord(알파벳)->숫자
    #chr(숫자)->알파벳
    answer = ''
    for alpha in s: 
        if alpha.isupper():
            word = chr((ord(alpha)-ord('A')+n)%26 + ord('A'))
        elif alpha.islower():
            word = chr((ord(alpha)-ord('a')+n)%26 + ord('a'))
        else:
            word = ' '
        answer += word
    return answer