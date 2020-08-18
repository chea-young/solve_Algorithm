def solution(msg):
    word = ['A','B','C','D','E','F','G','H','I','J','K','L',
            'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    answer = []
    index = 0
    find = ''
    while(index != len(msg)):
        find += msg[index]
        if(find in word):
            index += 1
            if(index==len(msg)):
                answer.append(word.index(find) +1)
                word.append(find)
        else:
            answer.append(word.index(find[:len(find)-1]) +1)
            word.append(find)
            find = ''
    return answer
            
print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))