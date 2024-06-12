# 2020 카카오 인턴십

def solution(numbers, hand):
    answer = ''
    
    keypad={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],0:[3,1]}
    l_hand=[3,0]
    r_hand=[3,2]
    
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            l_hand=keypad[i]
        elif i in [3,6,9]:
            answer+='R'
            r_hand=keypad[i]
        else:
            d_l=abs(keypad[i][0]-l_hand[0])+abs(keypad[i][1]-l_hand[1])
            d_r=abs(keypad[i][0]-r_hand[0])+abs(keypad[i][1]-r_hand[1])
            if d_l<d_r:
                answer+='L'
                l_hand=keypad[i]
            elif d_l>d_r:
                answer+='R'
                r_hand=keypad[i]
            else:
                if hand=='right':
                    answer+='R'
                    r_hand=keypad[i]
                else:
                    answer+='L'
                    l_hand=keypad[i]
            
    return answer