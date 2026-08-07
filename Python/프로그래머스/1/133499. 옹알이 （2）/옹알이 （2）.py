def solution(babbling):
    cnt = 0
    able_word = ['aya', 'ye', 'woo', 'ma']
    for word in babbling:
        for aw in able_word:
            if aw*2 in word:
                break
            word = word.replace(aw, ' ')
        if word.strip() == '':
            cnt += 1
    return cnt