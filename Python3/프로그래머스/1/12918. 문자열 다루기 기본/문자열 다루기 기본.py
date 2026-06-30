def solution(s):
    #길이가 4 혹은 6, 숫자로만 구성 
    if len(s)==4 or len(s)==6:
        if s.isdigit():
            return True
    return False