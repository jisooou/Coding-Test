def solution(babbling):
    cnt = 0
    able = ['aya', 'ye', 'woo', 'ma']
    for word in babbling:
        for able_word in able:
            if able_word*2 in word:
                break
            word = word.replace(able_word, ' ')
        if word.strip() == '':
            cnt += 1
    return cnt
                
    