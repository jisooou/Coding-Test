def solution(record):
    #1. 변수 정하기, 입력값 나누기 
    #2. 아이디가 같으면 마지막 이름으로 변경  
    #3. 변수에 따른 한국어 출력
    name_list = {}
    result = []
    
    for i in record: 
        parts = i.split()
        type = parts[0]
        id = parts[1]
        
        if type=='Enter' or type=='Change':
            name = parts[2]
            name_list[id] = name
            
    for i in record:
        parts = i.split()
        type = parts[0]
        id = parts[1]
        
        if type=='Enter':
            result.append(name_list[id]+'님이 들어왔습니다.')
        elif type=='Leave':
            result.append(name_list[id] +'님이 나갔습니다.')
    return result
    