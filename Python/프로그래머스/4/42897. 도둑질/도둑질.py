def solution(money):
    m = len(money)
    #첫번째 집O 
    dp1 = [0]*m #[0000]
    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2, m-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
    
    #첫번째 집X
    dp2 = [0]*m
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, m):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
    
    return max(dp1[m-2], dp2[m-1])