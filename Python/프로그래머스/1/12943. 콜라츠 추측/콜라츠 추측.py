def solution(num):
    def dfs(number, cnt):
        if number == 1:
            return cnt
        if cnt == 500:
            return -1
        
        if number % 2 == 0:
            return dfs(number//2, cnt+1)
        else:
            return dfs(number*3+1, cnt+1)
    return dfs(num, 0)