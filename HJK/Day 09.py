#%% (1) list tast
#자연수를 한글로 변환
num = int(input("변환할 자연수 입력 : "))
hangle = "공일이삼사오육칠팔구"
result = ""

while num != 0 :
    result = hangle[num % 10] + result
    num = num // 10

print(result)
#%% (2) mutable, immutable

# mutable(변할수있는) : list
datalist1 = [1,2,3]
datalist2 = datalist1
datalist2.append(4)

print(datalist2)
print(datalist1)
# immutable(변할수 없는) : tuple
datatuple = (1,2,3)

#%% (3) dict tast
china = {"자장면" : 4500, "짬뽕" : 16000, "울면" : 7200}
china["탕수육"] = 16000
china["자장면"] = 5000
del china["울면"]

print(china.keys())
#%% (4)

#%% (5)


