#%% (1) 출력연습
# print("hongjoonki")
# 이름을 출력하는 부분
name = "홍준기"
print("저의 이름은", name)
# 나이를 출력하는 부분
age = int(18)
print("저의 나이는", age, "살 입니다.")

#%% (2) 자료형
num = 10.9
print(type(num))

text = "s"
print(type(text))

#%% (3) 변수연습
name = "홍준기"
age = 18
height = 170.2
hobby = "자전거"

# print("저의 이름은", name)
# print("저의 나이은", age)
# print("저의 키는", height)
# print("저의 취미는", hobby)
# print(name,emd= "/")
# print(age,emd= "/")
# print(height,emd= "/")
# print(hobby)
print(name, age, height, hobby, sep= "/")
#%% (4) 형변환
# 자동 형변환
print(type(3 + 0.3)) # 값은 실수
print(type(3 + 3))   # 값은 정수

# / : 나눗셈 몫과 나머지 구하는 연산자
print(10/3)
# // : 나눗셈 몫을 구하는 연산자
print(10//3)
# % : 나눗셈 나머지을 구하는 연산자
print(10%3)

# 강제 형변환
print(int(10.98))

print(ord("b"))
#%% (5) 서식문자
# %f 같은 경우는 소수 2자리 까지
name = "홍준기"
age = 18
height = 170.2
hobby = "자전거"

print("이름 : %s" %name)
print("나이 : %d살" %age)
print("키 : %.1f" %height)
print("취미 : %s" %hobby)
#%% (6) 포멧(format)
#문자열값.format()
# A.B : A안에 B

data1 = 10
data2 = 10.4321
data3 = "A"
data4 = "ABC"

print("data1 : {}".format(data1))
print("data2 : {}".format(data2))
print("data3 : {}".format(data3))
print("data4 : {}".format(data4))

print("data1 : {}, data2 : {}, data3 : {}, data4 : {}".format(data1, data2, data3, data4))

#%% (7) 암호화 
pw = "rbgu123"
en_pw = ""

for i in pw:
    en_pw += chr(ord(i) * 9)
    
print("초기 비밀번호 : {}".format(pw))
print("암호화된 비밀번호 : {}".format(en_pw))


