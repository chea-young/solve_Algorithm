# 허프만 코드는 가장 높은 빈도에서 발생하는 문자를 가장 짧은 코드로 할당하여 텍스트를 압축한다.
def decode(codes, encoded):
    max_char = 0
    info = {}
    for i in codes:
        item = i.split('\t')
        if(max_char< len(item[1])):
            max_char = len(item[1])
        info[item[1]] = item[0]
    print(max_char, info)
    answer = ''
    start = 0
    while(start != len(encoded)):
        for i in range(max_char, 0, -1):
            start_index = start
            end_index = start+i
            item = ''
            try:
                item = info[encoded[start_index:end_index]]
            except:
                continue
            if(item == '[newline]'):
                answer += '\n'
            else:
                answer += item
            start = end_index
            break
    return answer

print(decode(['a\t100100', 'b\t100101', 'c\t110001', 'd\t100000', '[newline]\t111111', 'p\t111110', 'q\t000001'],
'111110000001100100111111100101110001111110'))