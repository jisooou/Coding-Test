T = int(input())
for _ in range(T):
    N = int(input())
    total = 0
    while(N > 0):
        N //= 5
        total += N
    print(total)