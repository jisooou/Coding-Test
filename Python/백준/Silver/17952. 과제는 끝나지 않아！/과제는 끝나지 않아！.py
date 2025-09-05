import sys 

def solve():
    input = sys.stdin.readline
    n = int(input()) # 첫 입력을 받는다
    stack = []
    total_score = 0 
    for _ in range(n):
        #3개의 입력을 쪼개서 받아야 한다. 
        data = list(map(int, input().split()))
        #새로운 과제가 주어진 경우
        if data[0] == 1: 
            _, score, time = data
            stack.append([score, time])
        #진행중인 과제가 있는 경우 
        if stack: 
            #time: [1], score [0]
            #현재 과제에 대한 정보를 pop한다. 
            current_task = stack[-1]
            #현재 과제의 시간을 줄인다. 
            current_task[1] = current_task[1] - 1
            #만약 현재 과제 시간이 0이라면 점수를 더해야한다. 
            if current_task[1] == 0: 
                total_score = total_score + current_task[0]
                stack.pop()
    return total_score
    
print(solve())