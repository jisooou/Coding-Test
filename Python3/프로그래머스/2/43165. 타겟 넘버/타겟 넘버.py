def solution(numbers, target):
    cnt = 0
    def dfs(location, total):
        nonlocal cnt
        if location == len(numbers):
            if total == target:
                cnt += 1
            return
        dfs(location+1, total+numbers[location])
        dfs(location+1, total+(-numbers[location]))
    dfs(0, 0)
    return cnt