#%% Exception test

while True:
    a = int(input(">>"))
    if a == 0:
        break
    else:
        try:
            b = int(input(">>"))
        except ValueError :
            print("숫자만 입력해주세요")
        
    result = 0
        
    def divide(num1,num2):
        result = num1 // num2
        return result
    try :
        print(divide(a, b))
    except ZeroDivisionError :
        print("0으로 나눌 수 없습니다.")
    
    except SyntaxError :
        print("입력하신 숫자가 알맞게 되어 있나요?")
#%% (2) 비속어 필터
class NickNameError(Exception) :
    pass

def check(name) :
    if name in "바보" and name in "멍청" :
        raise NickNameError 
    
nickname = input()
#%% (3) 채팅 필터
class BadWordError(Exception) :
    pass

chat = ""

def checkChat(text) :
    badWords = ["바보", "멍청", "똥개"]
    for i in badWords :
        if i in text :
            global chat
            chat = text.replace(i,"**")
            raise BadWordError()
            
cut = 0
while True :
    chat = input("채팅[나가기:q] : ")
    if chat.lower() == 'q' or cut == 5:
        bool()
    
    try : 
        checkChat(chat)
        print(chat)
    except BadWordError :
        cut += 1

        print("%d회 비속어를 사용했습니다. \n 5회 경고 후 강제 퇴장됩니다. \n %d회 남았습니다. " %(cut, 5-cut)) 
        print(chat + "\n")



    
