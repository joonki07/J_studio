#%% (1) 제어문자
# 반드시 따옴표 안에서 사용한다.
# \n : 줄바꿈, 개형문자 (now line)
# \t : 
# \\ : \ 표현
#%% (2) 입력
# 커서가 깜박이는 상태
# input(출력할 메세지)
Name = input("이름 : ")
print("이름는 %s 입니다." %Name)
#%% (3) 사칙 연산(산술 연산자)
#

num1 = int(input("정수1 : "))
num2 = int(input("정수2 : "))
# input("내용") 은 문자가 된다 그러므로
# int(input())
add = num1 + num2
sud = num1 - num2
mul = num1 * num2
div = num1 // num2
mod = num1 % num2

print("%d + %d = %d" %(num1, num2, add))
print("%d - %d = %d" %(num1, num2, sud))
print("%d * %d = %d" %(num1, num2, mul))
print("%d // %d = %d" %(num1, num2, div))
print("%d %% %d = %d" %(num1, num2, mod)) 

#%% (4) 조건식
isok = True
isok = False

print(type(isok))

#%% (5) 관계 연산자
exl = 10 == 11
exl = 10 != 11

print(exl)

#%% (6) 논리 연산자
exl = 10 == 11 and 10 > 1

print(exl)
#%% (7) 실수 연산의 오류와 해결방법
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
# 컴퓨터는 

# 첫번째 방법
import math

print(math.isclose(0.1 + 0.2, 0.3))
# 두번째 방법
from decimal import Decimal 
print(float(Decimal("0.1") + Decimal("0.2")))
#%% (8) 예제
num1 = float(input("첫 번쨰 실수를 입력하시오 : "))
num2 = float(input("두 번쨰 실수를 입력하시오 : "))


add = num1 + num2
print("%.2f와 %.2f의 합은 %.2f입니다" %(num1, num2, add))