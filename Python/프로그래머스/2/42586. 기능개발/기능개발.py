def solution(progresses, speeds):
    lst = []
    for progress, speed in zip(progresses, speeds):
        remain = 100-progress
        if remain%speed==0:
            lst.append(remain//speed)
        else:
            lst.append(remain//speed+1)
    
    before = lst[0]
    cnt = 1
    answer = []
    for i in range(1, len(lst)):
        if before >= lst[i]:
            cnt += 1
        else:
            answer.append(cnt)
            before = lst[i]
            cnt = 1
    answer.append(cnt)
    return answer
            