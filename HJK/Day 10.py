#%% (1) dicttask
#학생 이름과 학생 점수를 입력 받고
# 추가, 수정, 삭제
title = "\n\n☆학생성적관리 프로그램☆\n"
msg = "1.추가\n2.수정\n3.삭제\n4.목록\n5.나가기\n>>>"
student = {}
subject = ["국어", "영어", "수학"]

while True:
    choice = int(input(title + msg))

    #추가
    if choice == 1 :
        name = input("추가할 학생 이름 : ")
        if name not in student:
            student[name] = input("다음과 갗이 각 점수를 입력해주세요\n ex)국어,영어,수학\n").split(",")
        else:
            print("이미 등럭된 학생입니다.")
        print(student)
    #수정
    elif choice == 2 :
        choice = int(input("\n1.학생명\n2.점수"))
        name = input("수정할 학생 이름 : ")
        if choice == 1:
            if name in student:
                new = input("새로운 이름 : ")
                score = student[name]
                del student[name]
                student[new] = score
            else:
                print("없는 학생이름 입니다.")
        elif choice == 2:
            choice = int(input("1.국어\n2.영어\n3.수학\n"))
            student[name][choice-1] = int(input("세로운 점수 : "))
        else:
            print("다시 입력해 주세요.")
            
    elif choice == 3 :
        name = input("삭제할 학생 이름 :")
        if name in student:
            del student[name]
        else:
            print("없는 학생이름 입니다.")
        print(student)
    #목록
    elif choice == 4 :
        for i in student.keys() :
            print("◁" + i + "▷")
            num = 0
            for j in student[i] :
                print(subject[num] + " : " + str(j) + "점")
                num += 1
    #나가기
    elif choice == 5 :
        break
    #그 외
    else:
        print("다시 입력해 주세요.")

