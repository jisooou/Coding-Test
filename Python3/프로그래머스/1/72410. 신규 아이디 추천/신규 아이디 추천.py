def solution(new_id):
    s = new_id.lower()
    
    allow = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    temp = ''
    for i in s:
        if i in allow:
            temp += i 
    s = temp 
    
    while '..' in s:
        s = s.replace('..', '.')
    s = s. strip('.') 
    if s == '':
        s = 'a'
    if len(s) >= 16:
        s = s[:15]
        s = s.rstrip('.')
    while len(s)<3:
        s += s[-1]
    
    return s