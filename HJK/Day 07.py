#%% (1) 기타 제어문
#%% (2) 
for num in range(100):
    if (num+1)%3 != 0 or (num+1)%5 != 0:
        continue
    print(num+1)
#%% (3) while task

# 이름을 10번 출력
# for i in range(10):
#     print("joonki")
    
cnt = 0

while cnt != 10 :
    cnt += 1
    print("joonki")

#%% (4) 혈액형 조사

# choice = int(input("당신의 혈액형은?\n1.A형\n2.B형\n3.O형\n4.AB형\n >>>"))

ansA = "섬세하다"
ansB = "거침없고 추진력이 좋다"
ansO = "샤교성이 좋다"
ansAB = "착하다"
errmsg = "다시 입력"

while True:
    choice = int(input("당신의 혈액형은?\n1.A형\n2.B형\n3.O형\n4.AB형\n >>>"))
   
    if choice == 1:
        print(ansA)
    elif choice == 2:
        print(ansB)
    elif choice == 3:
        print(ansO)
    elif choice == 4:
        print(ansAB)
    elif choice == 0:
        print("질문을 종료합니다.")
        break
    else: 
        print(errmsg)
        
#%% (5) list
datalist = [1, 2, 3]

datalist.append(4)
datalist.insert(2, 6)

print(datalist)

