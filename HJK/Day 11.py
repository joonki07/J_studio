#%% (1) 함수
# 두 정수의

# 1. 메소드 이름을 생각한다.
# 2. 매개변수를 생각한다.
# 3. 실행할 문장을 생각한다.
# 4. 반환 값을 생각한다.

def add(num1, num2):
    result = num1 + num2
    return result

add(2,5)
#%% (2) method task
# 1~100
def print1to100():
    for i in range(100):
        print(i+1, end= " ")
        
print1to100()

#%% 1~10
def sum1to10():
    result = 0
    for i in range(10):
        result += (i+1)
    return result
    
sum1to10()
#%% 자연수를 음수로
def changeTonegative(num):
    result = 0
    
    if num > 0:
        result = num * -1
    else:
        result = False
        
    return result

print(changeTonegative(6))

#%% 1~n

def sum1toN(num):
    result = 0
    for i in range(num):
        result += (i+1)
    print(result)
    
sum1toN(4)

#%% 홀수 <=> 짝수
def evenOrOdd(num):
    if num % 2 == 0:
        result = num + 1
    else:
        result = num + 1
    return result

print(evenOrOdd(6))

#%% a~b 합

def sumAtoB(a,b):
    result = 0
    for i in range(a,b+1):
        result += (i+1)
    print(result)
    
sumAtoB(4,9)