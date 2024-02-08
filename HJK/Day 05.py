#%% 1
num = int(input("10~99 사이의 정수를 입력하세요 \n>>>"))
ten = num//10
one = num%10
print("십의자리 : %d" %ten)
print("일의자리 : %d" %one)

#%% 2
second = int(input("초를 입력하세요 \n>>>"))
minute = second%3600//60
hour = second//3600
second = second%60

print("변환 결과는 %d시간 %d분 %d초입니다." %(hour, minute, second))

#%% 3
num1 = int(input("사원 번호를 입력하시오 >>>"))

num2 = num1%10

num3 = ("오전"if num2 >= 5 else "오후")

print("근무 시간은 %s입나다" %num3)
#%% 4
import math
noodles = int(input("라면의 개수를 입력하시오 \n >>>"))

boxnum = int(math.ceil(noodles/20))

print("%d개의 라면을 담으려면 %d개의 박스가 필요합니다." %(noodles, boxnum))



#%% 5
korean = int(input("국어 점수 : "))
english = int(input("영어 점수 : "))
math = int(input("수학 점수 : "))

issum = (korean + english + math)
average = issum/3
if average >= 80:
    result = "합격"
else :
    result = "불합격"
    
print("평균은 %.2f점이고, 결과는 %s입니다." %(average, result))
#%% 6
age = int(input("당신의 나이는 어떻게 되나요? \n >>>"))

if age < 8:
    state = "미취학아동"
elif (age >= 8 and age < 13):
    state = "초등학생"
elif (age >= 13 and age < 17):
    state = "중학생"
elif (age >= 17 and age < 20):
    state = "고등학생"
else:
    state = "성인"

print("아! 당신은 %s이군요" %state)
