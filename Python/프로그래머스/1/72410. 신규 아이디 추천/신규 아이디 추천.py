def solution(new_id):
    #1
    s = new_id.lower()
    
    #2
    allow = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    temp = ''
    for i in s:
        if i in allow:
            temp += i
    s = temp 
    
    #3
    while '..' in s:
        s = s.replace('..', '.')
    
    #4
    s = s.strip('.')
    
    #5
    if s == '':
        s = 'a'
        
    #6
    if len(s) >= 16:
        s = s[:15]
        s = s.rstrip('.')
    
    #7
    while len(s)<3:
        s += s[-1]
        
    return s