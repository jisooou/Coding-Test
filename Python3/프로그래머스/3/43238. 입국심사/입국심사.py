def solution(n, times):
    left = 1
    right = max(times) * n
    answer = right
    
#     중간 지점의 시간을 파악 -> 거기까지 몇명을 수용할 수 있는지
    while left <= right:
        mid = (left+right)//2
        people = 0 
        
        for t in times:
            people += mid // t
            
        if people >= n:
            answer = mid 
            right = mid - 1
        elif people < n:
            left = mid + 1
    return answer