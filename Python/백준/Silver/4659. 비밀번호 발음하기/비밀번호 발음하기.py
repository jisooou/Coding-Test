while(True):
    s = input()
    if s == "end":
        break 
        
    prev = ''
    has_vowel = False
    vowel_cnt = 0
    cons_cnt = 0
    ans_yes = True
        
    for ch in s: 
        if ch == prev and ch not in 'eo':
            ans_yes = False
        if ch in 'aeiou':
            has_vowel = True
            vowel_cnt += 1
            cons_cnt = 0 
        else: 
            cons_cnt += 1
            vowel_cnt = 0 
    
        if vowel_cnt == 3 or cons_cnt == 3: 
            ans_yes = False 
    
        prev = ch 
    if not has_vowel: 
        ans_yes = False 

    if ans_yes: 
        print(f"<{s}> is acceptable.")
    else: 
        print(f"<{s}> is not acceptable.")