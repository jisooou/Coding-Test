#my_string에서 각 문자를 n만큼 반복해서 리턴
def solution(my_string, n):
    answer = ''
    for w in my_string: 
        answer += w * n
    return answer