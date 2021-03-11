question_1 = [1,2,4,2,1,3,2,4,1,3,2,2,2,4,3,3,4,2,4,3]
question_2 = [2,4,4,3,4,4,2,2,1,4,1,3,4,1,3,4,2,1,4,3]
question_3 = [2,1,4,3,4,1,3,2,1,3,1,4,1,3,1,4,3,3,4,3]
question_4 = [2,3,2,3,1,2,2,4,1,1,1,3,1,4,1,4,3,4,1,3]
question_5 = [1,3,4,3,3,4,3,3,4,4,4,1,1,3,2,2,1,1,4,2]


answer_1 = [1,2,4,4,1,3,4,4,1,2,2,2,1,4,3,3,4,2,4,3]
answer_2 = [2,4,4,3,3,3,2,2,1,3,1,3,4,1,3,1,2,1,1,3]
answer_3 = [2,1,4,1,4,2,3,2,1,3,1,4,1,3,2,4,1,3,4,1]
answer_4 = [2,4,2,3,1,1,2,4,1,1,1,3,2,4,1,4,3,4,4,3]
answer_5 = [2,3,4,3,3,4,3,3,2,4,1,2,1,1,2,1,2,1,4,1]
score = 0
for number in range(1, 6):
    answer = []
    question = []
    if number == 1:
        answer = answer_1
        question = question_1
    elif number ==2:
        answer = answer_2
        question = question_2
    elif number ==3:
        answer = answer_3
        question = question_3
    elif number ==4:
        answer = answer_4
        question = question_4
    elif number ==5:
        answer = answer_5
        question = question_5
    
    right = 0
    error = ""
    for index in range (0, 20):
        if(answer[index] == question[index]):
            right +=1
        else :
            error += str(index+1) + " "
    print("과목" + str(number) + " = " + str(right*5) + " 틀린 번호는 "+ error)
    score += right *5
print("평균은 "+ str(score/5))