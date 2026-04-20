# +K , *2
# n까지 돌면서 *2 한 후에 남은 거 +K 만큼 => 최소
def solution(n):
    ans = 0
    while n > 0: 
        ans += n % 2
        n //= 2   
    return ans