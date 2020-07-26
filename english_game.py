def solution(n, words):
    stage = 0
    num = 0
    f_word = words[num]
    w = []
    w.append(f_word)
    while(True):
        stage += 1
        if(stage != 1):
            if(f_word[-1] == words[num][0] and words[num] not in w):
                f_word = words[num]
                w.append(f_word)
            else:
                return [1,stage]
        for i in range(1,n):
            if(f_word[-1] == words[num+i][0] and words[num+i] not in w):
                f_word = words[num+i]
                w.append(f_word)
                continue
            else:
                return [i+1,stage]
        num +=n
        if(num == len(words)):
            return [0,0]

print(solution(3,['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(5,['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']))
print(solution(2,['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))