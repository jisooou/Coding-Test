def solution(progresses, speeds):
    stack = []
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        if remain % speeds[i] == 0:
            stack.append(remain // speeds[i])
        else:
            stack.append((remain // speeds[i])+1)
            
    answer = []
    current = stack[0]
    cnt = 1
    for s in range(1, len(stack)):
        if stack[s] <= current:
            cnt += 1
        else:
            answer.append(cnt)
            current = stack[s]
            cnt = 1
    answer.append(cnt)
    return answer
    