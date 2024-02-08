#%% updown

import random as r
import time

answer = r.randint(1, 100)

print("UpDown 게임 시작")
start = time.time()
cnt = 0

while True:
    msg = int(input("정답을 말해주세요\n>>>"))
    cnt += 1
    if msg == answer:
        print("정답입니다.")
        break
    elif msg > answer:
        print('Down')
    else:
        print('Up')
end = time.time()

elapse = end - start
print("%d초 만에 성공!!"%elapse)
print("%d번 만에 성공!!"%cnt)
