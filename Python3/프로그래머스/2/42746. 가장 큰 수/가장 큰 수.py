def solution(numbers):
    #문자열로 리턴
    str_num = list(map(str, numbers))
    lst = sorted(str_num, reverse=True, key=lambda x: x*3) 
    if lst[0] == '0':
        return '0'
    return ''.join(lst)