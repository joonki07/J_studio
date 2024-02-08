#%%(1) method task
# 정수 리스트를 오름차순으로 정렬하는 메소드
datalist = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def sortASC(numlist):
    for i in range(len(datalist)-1):
        for j in range(i + 1, len(numlist)):
            if numlist[i]>numlist[j]:
                temp = numlist[i]
                numlist[i] = numlist[j]
                numlist[j] = temp
                
sortASC(datalist)
print(datalist)

#%% method task
#소문자를 대문자로 바꿔주는 메소드
# A = 65 a~z = 97~122         -32

def changeToUpper(string):
    result = ""
    for i in string:
        if ord(i) >= 97 and ord(i) <= 122:
            result += chr(ord(i) - 32)
        else: 
            result += i
    return result

print(changeToUpper('fafafafd'))
#%%(3) method task
#한글로 정수를 입력하면 숫자로 

def changeToInt(string):
    hanglelist = "공일이삼사오육칠팔구"
    result = ""
    for i in string : 
        result += str(hanglelist.index(i))
    return int(result)

print(changeToInt("일구사오")+55)

#%% (4) 지역변수와 전역변수

# def add(num1, num2 = 0):
#     return num1 + num2

# def sud(num1, num2 = 0):
#     return num1 - num2

# def multi(num1, num2 = 1):
#     return num1 * num2

# 전역 변수란 (전 지역변수) 
# num1과 num2를 계속해서
#%%
result = 0

def add2(num1, num2 = 0):
    global result
    result = num1 + num2
    
def sud2(num1, num2 = 0):
    global result
    result = num1 - num2
    
def multi2(num1, num2 = 1):
    global result
    result = num1 * num2


    global result
    result = num1 - num2
#==================================================
#                      전역변수            지역변수
# 함수 안에서 읽기        가능                가능
# 함수 안에서 수정        불가능              가능
#
# 함수 밖에서 읽기 
# 함수 밖에서 수정 
#===================================================