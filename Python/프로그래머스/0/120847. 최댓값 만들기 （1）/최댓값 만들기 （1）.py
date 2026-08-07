def solution(numbers):
    #오름차순 정렬 -> 마지막 두 개 원소 곱해서 return 
    num_sort = sorted(numbers)
    last_num = num_sort[-1]
    last_next_num = num_sort[-2]
    answer = last_num * last_next_num
    return answer