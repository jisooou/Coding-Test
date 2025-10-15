#완전탐색 문제
#조건1.brown = 세로는 무조건 3이상이어야 한다. 
#조건2.return 값에 [4,3]-[x,y] : (x-2)*(y-2) = yellow

import math 
def solution(brown, yellow):
    total = brown + yellow #12
    #세로를 기준으로 한다. 세로 무조건 3이상. 
    #약수 쌍 구할 때: 제곱수까지만 순회
    #조건1
    for height in range(3, int(math.sqrt(total)+1)):
        if total % height == 0: 
            width = total // height
            #조건2
            if (width-2)*(height-2) == yellow: 
                return [width, height]