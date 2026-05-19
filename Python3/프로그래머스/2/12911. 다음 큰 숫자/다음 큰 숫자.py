def solution(n):
    answer = 0
    nxt = n + 1
    cnt_n = bin(n).count('1')
    while True:
        cnt_ans = bin(nxt).count('1')
        if cnt_n == cnt_ans:
            return nxt
        nxt += 1