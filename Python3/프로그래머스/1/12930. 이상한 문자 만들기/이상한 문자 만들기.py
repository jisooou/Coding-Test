def solution(s):
    answer = ''
    idx = 0
    for word in s:
        if word == ' ':
            answer += word
            idx = 0
        else:
            if idx % 2 == 0:
                answer += word.upper()
            else:
                answer += word.lower()
            idx += 1
    return answer