def solution(files):
    info = []
    num_len = 0
    for f in range(len(files)):
        head = ''
        num = ''
        check = False
        for name in files[f]:
            if(name.isdigit()):
                num+= name
                check = True
            else:
                if(check==True):
                    break
                head+=name
        if(num[0] == '0'):
            num = num[1:]
        if (num_len < len(num)):
            num_len = len(num)
        info.append([head.lower(), num,f, files[f]])
    for i in info:
        i[1] = (num_len-len(i[1]))*'0'+i[1]
    answer = sorted(info, key=lambda x: (x[0],int(x[1]),x[2]))
    return [i[3] for i in answer]

print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution( ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
        