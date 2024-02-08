#%% for
#///////////////////////////////////////
#초기값을 생략하면 0이 들어간다.


# startnum = int(input(""))
# for i in range(11)

for i in range(10):
    
    print("%d" %(10-i))

#%% 1
for i in range(100):
    
    print(i+1, end= " ")
#%% 2
for i in range(100):
    
    print(100-i, end= " ")
#%% 3
for i in range(100):
    if i % 2 == 0:
        print(i+2, end= " ")
#%% 4
for i in range(6):
    
    print(chr(i+65))

#%% 5
for i in range(6):
    if i != 2:
        print(chr(i+65))

#%% 6
for i in range(26):
    if i%2 != 0:
        print(chr(i+65))
    else:
        print(chr(i+97))

#%% 7
num = int(input("점수를 입려해주세요 : "))
if num >= 90:
    credit = "A"
elif num < 90 and num >=80:
    credit = "B"
elif num < 80 and num >=70:
    credit = "C"
elif num < 70 and num >=60:
    credit = "D"
else:
    credit = "F"
print("점수는 %d이고, 학점은 %s학점입니다." %(num, credit))
#%% 8
num1 = int(input("정수를 입력하시오 >>>"))

if num1 % 3 == 0:
    result = "입니다."
else:
    result = "가 아닙니다."

print("%d는 3의 배수%s" %(num1, result))
#%% 9
num1 = int(input("정수1 입력 >>>"))
num2 = int(input("정수2 입력 >>>"))
num3 = int(input("정수3 입력 >>>"))

if num1 > num2:
    print(num1)


