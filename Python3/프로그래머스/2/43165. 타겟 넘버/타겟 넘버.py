def solution(numbers, target):
    answer = 0
    def dfs(location, total):
        nonlocal answer
        if location == len(numbers):
            if total == target:
                answer += 1
            return 
        dfs(location+1, total+numbers[location])
        dfs(location+1, total+(-numbers[location]))
    dfs(0, 0)
    return answer