def solution(n):
    state = 'move'
    energy = 1
    move = 2
    n-=2
    while(n!=0):
        if(state == 'move'):
            if(n-move<0):
                state = 'jump'
                move=1
            else:
                n-= move
                move *=2
        if(state == 'jump'):
            state = 'move'
            energy +=1
            n-=1
    return energy

print(solution(5))
print(solution(6))
print(solution(5000))