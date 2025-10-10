# f-string 사용

def solution(s):
    num_list = list(map(int, s.split()))
    answer = f"{min(num_list)} {max(num_list)}"
    return answer