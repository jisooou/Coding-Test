# 재귀호출을 하면 시간초과
def solution(n):
    answer = [0, 1]
    for i in range(2, n+1):
        answer.append((answer[i-1]+answer[i-2]) % 1234567)
    return answer[-1]