def solution(n):
    answer = []
    def hanoi(num, start, end, mid):
        if num == 1:
            answer.append([start, end])
            return
        hanoi(num-1, start, mid, end)
        answer.append([start, end])
        hanoi(num-1, mid, end, start)
    hanoi(n, 1, 3, 2)
    return answer