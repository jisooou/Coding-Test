def solution(n):
    cnt_bin = bin(n).count('1')
    nxt = n + 1
    while True:
        nxt_cnt = bin(nxt).count('1')
        if cnt_bin == nxt_cnt:
            return nxt
        nxt += 1
        