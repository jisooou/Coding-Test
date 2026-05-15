def solution(n):
    result = 0
    for i in range(1, n+1):
        total = 0
        for num in range(i, n+1):
            total += num
            if total == n:
                result += 1
                break

            if total > n:
                break
    return result 