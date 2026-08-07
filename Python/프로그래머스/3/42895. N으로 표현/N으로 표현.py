def solution(N, number):
    dp = [set() for i in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        for j in range(1, i):
            for first in dp[j]:
                for second in dp[i-j]:
                    dp[i].add(first+second)
                    dp[i].add(first-second)
                    dp[i].add(first*second)
                    if first != 0 and second != 0:
                        dp[i].add(first//second)
        if number in dp[i]:
            return i 
    return -1