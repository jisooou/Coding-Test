# 인덱스값을 뽑아올 수 있는지
def solution(num, k):
    str_num = str(num)
    for i, value in enumerate(str_num):
        if value == str(k):
            return (i+1)
    return -1