def solution(record):
    name_lst = {}
    result = []
    for i in range(len(record)):
        parts = record[i].split()
        command = parts[0]
        id = parts[1]
        
        if command == 'Enter' or command == 'Change':
            name = parts[2]
            name_lst[id] = name
            
    for i in range(len(record)):
        parts = record[i].split()
        command = parts[0]
        id = parts[1]
        
        if command == 'Enter':
            result.append(name_lst[id] + '님이 들어왔습니다.')
        elif command == 'Leave':
            result.append(name_lst[id] + '님이 나갔습니다.')
    return result
            
    