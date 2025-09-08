#deque를 사용하여 더 효율적인 코드를 작성해 보자: from collectioins import deque
import sys
from collections import deque

q = deque()
max_len = 0 
back_num = 0 
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    num_list = input().split()
    #1이면 append
    if num_list[0] == '1': 
        q.append(int(num_list[1]))
        #최대길이를 계속 갱신을 해서 최대길이일 때와, 그때 맨뒤 학생번호를 알아야 한다. 
        # (예를 들어, 전체 길이가 초기화한 최대 길이보다 크다면 최대 길이가 전체 길이이다. 
        if len(q) > max_len:
            max_len = len(q)
            back_num = q[-1]
    #근데 만약 전체 길이와 최대 길이가 같다면 어떻게 할까?-> 최소 값을 출력하기로 했다)
        elif len(q) == max_len:
            back_num = min(back_num, q[-1])
    #2면 popleft
    else:
        q.popleft()
        
print(max_len, back_num)