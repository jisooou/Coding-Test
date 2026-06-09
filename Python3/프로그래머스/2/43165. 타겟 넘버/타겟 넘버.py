def solution(numbers, target):
    answer = 0
    def dfs(num, total):
        nonlocal answer
        if num == len(numbers):
            if total == target:
                answer += 1
            return 
        dfs(num+1, total+numbers[num])
        dfs(num+1, total+(-numbers[num]))
        
    dfs(0, 0)
    return answer