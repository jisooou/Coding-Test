# 수행시간- O(n^2): 초과 -> O(n√n): 개선

import math
def solution(number, limit, power):
    # 1. 1부터 number까지 수를 돈다. 
    # 2. 하나씩 돌면서 약수의 개수를 구한다. 
    #     1. 약수의 개수를 어떻게 구하는가? 
    #     예) 6이라면, 1부터 6까지 돌면서 6과 나눠떨어지는지 확인한다. 
    #         1. 나눠떨어지면, 나눠떨어지는 수를 구한다. 
    # 3. 만약 이때 나눠떨어지는 수들이 power보다 크면 power을 사용한다. 
    # 4. 나눠떨어지는 수와 power 대체된 수가 있으면 모두 더해서 result를 구한다.
    answer = 0
    for i in range(number+1): #print(i)->1,2,3,4,5
#         예: i = 4 
        cnt = 0
#      for문을 다 돌릴 경우: 시간 초과 
#      sqrt()한 수가까지만 돌린다. 예) i가 4일때, k는 1~3까지. 즉 1,2만 돈다. 
#      i가 k로 나눠떨어지면 약수인데, k가 1일 때 2 증가(1,4 쌍으로 나옴) 
#      k가 2일 때 1 증가: 즉 제곱수라는 말이다. 2 = 4 // 2 -> 제곱수
        for k in range(1, int(math.sqrt(i)) + 1): #1,2,3,4
            if(i % k == 0): #나눠떨어지면 약수 
                if(k == i // k): #제곱수일 때 
                    cnt += 1
                else:
                    cnt += 2
        if cnt > limit: 
            cnt = power
        answer += cnt
    
    return answer