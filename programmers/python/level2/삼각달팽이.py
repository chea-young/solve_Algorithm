def solution(n):
    number = 1
    now = 0
    height = 0
    total = sum([ i for i in range(1,n+1)])
    answer = [0 for i in range(total)]
    while number<=total :
        now = answer.index(0)
        height = find_height(now)
        try :
            answer[now] = number
            number = number+1
            while True :
                index = now+height
                if answer[index]!=0 :
                    break
                answer[index] = number
                number,now = (number+1, index)
                height = height +1
        except IndexError:
            print('err01 ', answer)
        
        try: 
            while True :
                index = now+1
                if answer[index]!=0 :
                    break
                answer[index] = number
                number,now = (number+1, index)
        except IndexError:
            print('err02 ', answer)
        
        try: 
            reversed_a = list(reversed(answer))
            now = total-(reversed_a.index(0)+1)
            height = find_height(now)
            if(answer[now] == 0):
                answer[now] = number
                number= number+1
            while True :
                index = now-height
                print(now, height, answer[index], answer)
                if answer[index]!=0 :
                    break
                answer[index] = number
                number,now = (number+1, index)
                height = height-1
        except IndexError:
            print('err03 ', answer)
        except ValueError:
            break
    return answer

def find_height(num):
    height = 0
    while (num-height>=0):
        num = num-height
        height = height+1
    return height

def test_sample():
    assert solution(4) == [1,2,9,3,10,8,4,5,6,7]
    assert solution(5) == [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
    assert solution(6) == [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]