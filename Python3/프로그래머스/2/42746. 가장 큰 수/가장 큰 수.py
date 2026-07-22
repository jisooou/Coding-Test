def solution(numbers):
    answer = ''
    number = sorted(numbers, key=lambda x: str(x)*3, reverse=True)
    for i in number:
        answer += str(i)
    if answer[0] == '0':
        return '0'
    return answer