h, w = map(int, input().split())
for _ in range(h):
    cloud = input().strip()
    answer = []
    last = -1
    for c in cloud: 
        if c == 'c':
            answer.append(0)
            last = 0
        if c == '.':
            if last == -1: 
                answer.append(-1)
                last = -1
            else: #c를 만난 경우를 이와 같이 경우를 나눈다
                last += 1
                answer.append(last)
    print(*answer)