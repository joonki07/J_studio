#%% (1) list tast 01
print("-"*20)
# num = int(input("검색할 번호"))
datalist = [2, 4, 5, 6]

print(len(datalist))
print(datalist[2])
print(datalist.index(5))
datalist.append(7)
datalist.insert(1,3)


print(datalist)
#%% (2) list tast 02
print("-"*20)
datalist = [0] * 100
datalist.insert(43,50)
datalist.insert(21,"피자")
datalist[77] = "ABC"
print(datalist)
print(len(datalist))
print(datalist.index(50))
print(datalist.index("피자"))
print(datalist.index("ABC"))

#%% (3) list tast 03
print("-"*20)
datalist = [0] * 100

for i in range(100):
    datalist[i] = i+1

print(datalist)
#%% (3-2)
print("-"*20)
datalist = [0] * 50

for i in range(50):
    datalist[i] = (i+1) * 2

print(datalist)
#%% (4) list tast 04
print("-"*20)
#%% (5) list tast 05
print("--"*20)
datalist = [""] * 6

for i in range(6):
    datalist[i] = (chr(i+65))
print(datalist)
#%% (5-2)
print("-"*20)
datalist = [""] * 26

for i in range(26):
    if i%2 != 0:
       datalist[i] = (chr(i+65))
    else:
        datalist[i] = (chr(i+97))
print(datalist)
#%% 8
name = "Hongjoonki"
print(name[0:4])
#%%
time = input("시간,분, 초 \n >>>")
print("%s시간 %s분 %s초" %(time[:2], time[2:4], time[4:]))









