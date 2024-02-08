#%% 로또 번호 추천
import random
import time

pot = [n for n in range(1, 46)]
jackpot = []
for n in range(1, 7) : 
    random.shuffle(pot)
    pick = pot.pop()
    print("{}번째 당첨번호는 {}입니다.".format(n, pick))
    jackpot.append(pick)
    time.sleep(0.6)
    
jackpot.sort()
    
print("이번 회차 당첨번호는 {}입니다".format(jackpot))