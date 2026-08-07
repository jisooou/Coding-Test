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
        if number in [1,4,7]:
            result += 'L'
            left = number
        elif number in [3, 6, 9]:
            result += 'R'
            right = number
        else:
            current_x, current_y = pad[number]
            left_x, left_y = pad[left]
            right_x, right_y = pad[right]
            
            left_distance = abs(current_x-left_x)+abs(current_y-left_y)
            right_distance = abs(current_x-right_x)+abs(current_y-right_y)
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