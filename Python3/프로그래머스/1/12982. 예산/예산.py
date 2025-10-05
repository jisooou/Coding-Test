def solution(d, budget):
    cnt = 0
    d_sort = sorted(d) #오름차순으로 정렬한다.[1,2,3,4,5]
    for i in d_sort: 
        budget -= i 
        if budget < 0: 
            break 
        cnt += 1 
    return cnt