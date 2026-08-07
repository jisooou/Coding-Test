def solution(wallet, bill):
    cnt = 0
    while min(wallet) < min(bill) or max(wallet) < max(bill):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        cnt += 1
    return cnt