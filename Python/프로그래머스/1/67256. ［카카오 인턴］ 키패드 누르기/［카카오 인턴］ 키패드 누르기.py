def solution(numbers, hand):
    pad = {
        1:(0,0),
        2:(0,1),
        3:(0,2),
        4:(1,0),
        5:(1,1),
        6:(1,2),
        7:(2,0),
        8:(2,1),
        9:(2,2),
        '*':(3,0),
        0:(3,1),
        '#':(3,2)
    }
    
    left = '*'
    right = '#'
    result = ''
    
    for number in numbers:
        if number in [1, 4, 7]:
            result += 'L'
            left = number
        elif number in [3, 6, 9]:
            result += 'R'
            right = number
        else:
            left_x, left_y = pad[left]
            right_x, right_y = pad[right]
            target_x, target_y = pad[number]
            
            left_distance = abs(left_x-target_x)+abs(left_y-target_y)
            right_distance = abs(right_x-target_x)+abs(right_y-target_y)
            
            if left_distance < right_distance:
                result += 'L'
                left = number
            elif left_distance > right_distance:
                result += 'R'
                right = number
            else:
                if hand == 'left':
                    result += 'L'
                    left = number
                elif hand == 'right':
                    result += 'R'
                    right = number
    return result