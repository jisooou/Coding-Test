T = int(input())
for _ in range(T):
    num = int(input())
    cnt = 0 
    while (num > 0):
        num //= 5
        cnt += num
    print(cnt)