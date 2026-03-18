while(True):
    prev = ''
    answer = True
    has_vowel = False
    vowel_cnt = 0
    cons_cnt = 0

    word = input()
    if word == 'end':
        break 
    
    for ch in word: 
        if ch == prev and ch not in 'eo':
            answer = False    
            
        if ch in 'aeiou':
            has_vowel = True
            vowel_cnt += 1
            cons_cnt = 0
        else: 
            cons_cnt += 1
            vowel_cnt = 0
        
        if vowel_cnt == 3 or cons_cnt == 3: 
            answer = False 
            
        prev = ch 
        
    if has_vowel == False: 
        answer = False
        
    if answer: 
        print(f"<{word}> is acceptable.")
    else: 
        print(f"<{word}> is not acceptable.")